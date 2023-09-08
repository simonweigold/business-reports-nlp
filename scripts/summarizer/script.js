document.addEventListener('DOMContentLoaded', () => {
    const summarizeButton = document.getElementById('summarizeButton');
    const userInput = document.getElementById('userInput');
    const summarizedText = document.getElementById('summarizedText');

    summarizeButton.addEventListener('click', async () => {
        // Bring text in right format
        const inputText = cleanText(userInput.value);

        // Summarize text
        const summary = await summarizeText(inputText);
        summarizedText.value = summary;
    });
});

function cleanText(text) {
    // Replace multiple spaces with a single space
    let cleaned = text.replace(/\s+/g, ' ');

    // Ensure one space after punctuation marks
    cleaned = cleaned.replace(/([.!?;,:])(\S)/g, '$1 $2');

    // Replace special symbol "" with "-"
    // cleaned = cleaned.replace(//g, '-');

    return cleaned;
}

async function summarizeText(text) {
    const response = await fetch('http://localhost:5000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
    });
    const data = await response.json();
    return data.summary;
}
