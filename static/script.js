document.addEventListener('DOMContentLoaded', function () {
    const addForm = document.getElementById('addForm');
    const itemInput = document.getElementById('itemInput');
    const itemsContainer = document.getElementById('items');

    addForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const itemText = itemInput.value.trim();
        if (itemText) {
            fetch('/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'item': itemText
                })
            })
            .then(response => response.json())
            .then(data => {
                const itemDiv = document.createElement('div');
                itemDiv.className = 'item';
                itemDiv.innerHTML = `<span>${data.item}</span><button class="deleteBtn" data-item="${data.item}">Delete</button>`;
                itemsContainer.appendChild(itemDiv);
                itemInput.value = '';
            })
            .catch(error => console.error('Error:', error));
        }
    });

    itemsContainer.addEventListener('click', function (e) {
        if (e.target.classList.contains('deleteBtn')) {
            const itemText = e.target.getAttribute('data-item');
            fetch('/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'item': itemText
                })
            })
            .then(() => {
                e.target.parentElement.remove();
            })
            .catch(error => console.error('Error:', error));
        }
    });
});
