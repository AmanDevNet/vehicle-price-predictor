
document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    // Convert numeric fields to numbers
    data.Year = parseInt(data.Year);
    data.Present_Price = parseFloat(data.Present_Price);
    data.Kms_Driven = parseInt(data.Kms_Driven);
    data.Owner = parseInt(data.Owner);

    const btn = document.querySelector('.btn-predict');
    const originalText = btn.innerText;
    btn.innerText = 'Calculating...';
    btn.disabled = true;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();

        if (result.error) {
            alert('Error: ' + result.error);
        } else {
            const resultContainer = document.getElementById('result');
            const predictionValue = document.getElementById('predictionValue');

            predictionValue.innerText = result.prediction.toFixed(2);
            resultContainer.classList.remove('hidden');
            resultContainer.scrollIntoView({ behavior: 'smooth' });
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching the prediction.');
    } finally {
        btn.innerText = originalText;
        btn.disabled = false;
    }
});
