function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();

    if (taskText === '') {
        alert('Please enter a task.');
        return;
    }

    const taskList = document.getElementById('taskList');

    // --- STEP 1: Create the main task item container ---
    const taskItem = document.createElement('div');
    
    // --- STEP 2: Configure the element (add class and content) ---
    taskItem.classList.add('task-item');
    
    // Create the span for the task text
    const taskTextSpan = document.createElement('span');
    taskTextSpan.textContent = taskText;
    
    // Create the delete button
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('delete-btn');

    // Add an event listener to the delete button using an arrow function
    deleteButton.onclick = function() {
        // When clicked, remove the parent element (the whole task item)
        taskList.removeChild(taskItem);
    };
    
    // Assemble the internal structure using appendChild
    taskItem.appendChild(taskTextSpan);
    taskItem.appendChild(deleteButton);

    // --- STEP 3: Insert the element into the DOM (append to the list) ---
    taskList.appendChild(taskItem);

    // Clear the input field for the next entry
    taskInput.value = '';
    taskInput.focus();
}
