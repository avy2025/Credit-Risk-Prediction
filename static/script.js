document.addEventListener('DOMContentLoaded', async () => {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');
    const submitBtn = document.getElementById('submit-btn');
    const resetBtn = document.getElementById('reset-btn');
    const meterFill = document.getElementById('meter-fill');
    const riskValue = document.getElementById('risk-value');
    const riskCategory = document.getElementById('risk-category');
    const confidenceScore = document.getElementById('confidence-score');

    let featureMetadata = {};

    // 1. Fetch feature metadata and build form
    try {
        const response = await fetch('/api/features');
        featureMetadata = await response.json();

        form.innerHTML = ''; // Clear loader

        for (const [name, meta] of Object.entries(featureMetadata)) {
            const group = document.createElement('div');
            group.className = 'form-group';

            const label = document.createElement('label');
            label.textContent = name.replace(/([A-Z])/g, ' $1').trim();
            group.appendChild(label);

            if (meta.type === 'categorical') {
                const select = document.createElement('select');
                select.name = name;
                select.required = true;
                meta.options.forEach(opt => {
                    const option = document.createElement('option');
                    option.value = opt;
                    option.textContent = opt;
                    select.appendChild(option);
                });
                group.appendChild(select);
            } else {
                const input = document.createElement('input');
                input.type = 'number';
                input.name = name;
                input.required = true;
                input.min = meta.min;
                input.max = meta.max;
                input.value = Math.floor((meta.min + meta.max) / 2);
                group.appendChild(input);
            }
            form.appendChild(group);
        }
    } catch (error) {
        console.error('Error loading features:', error);
        form.innerHTML = '<p class="error">Failed to load analysis parameters. Check backend.</p>';
    }

    // 2. Handle prediction
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        submitBtn.disabled = true;
        submitBtn.textContent = 'Analyzing...';

        const formData = new FormData(form);
        const data = {};
        for (const [key, value] of formData.entries()) {
            data[key] = featureMetadata[key].type === 'numerical' ? parseFloat(value) : value;
        }

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            showResult(result);
        } catch (error) {
            alert('Prediction failed. Ensure the server is running.');
            console.error(error);
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Run AI Prediction';
        }
    });

    function showResult(result) {
        resultContainer.classList.remove('hidden');
        form.parentElement.classList.add('hidden');

        const isBad = result.risk_category === 'Bad';
        const displayConf = (result.confidence * 100).toFixed(2);

        // Update Meter
        meterFill.className = 'meter-fill ' + (isBad ? 'bg-bad' : 'bg-good');
        meterFill.style.height = displayConf + '%';

        // Update Text
        riskValue.textContent = displayConf + '%';
        riskValue.className = isBad ? 'text-bad' : 'text-good';

        riskCategory.textContent = result.risk_category;
        riskCategory.className = 'value ' + (isBad ? 'text-bad' : 'text-good');

        confidenceScore.textContent = displayConf + '%';

        // Scroll to result
        resultContainer.scrollIntoView({ behavior: 'smooth' });
    }

    resetBtn.addEventListener('click', () => {
        resultContainer.classList.add('hidden');
        form.parentElement.classList.remove('hidden');
    });
});
