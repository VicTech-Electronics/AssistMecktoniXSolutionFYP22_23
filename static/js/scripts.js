function toggleButton(buttonId) {
    var button = document.getElementById(buttonId);
    
    if (button.value === 'Enabled') {
        button.style.backgroundColor = 'red';
        button.value = 'Disabled';
    } else {
        button.style.backgroundColor = 'green';
        button.value = 'Enabled';
    }
}