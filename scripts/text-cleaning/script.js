document.addEventListener('DOMContentLoaded', () => {
    const cleanTextButton = document.getElementById('cleanTextButton');
    const userInput = document.getElementById('userInput');
    const cleanedText = document.getElementById('cleanedText');

    cleanTextButton.addEventListener('click', () => {
        const inputText = userInput.value;
        let cleaned = cleanText(inputText);
        cleanedText.value = cleaned;
    });
});

function cleanText(text) {
    // Replace multiple spaces with a single space
    let cleaned = text.replace(/\s+/g, ' ');

    // Ensure one space after punctuation marks
    cleaned = cleaned.replace(/([.!?;,:])(\S)/g, '$1 $2');

    return cleaned;
}
