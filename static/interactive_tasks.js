// Проверка ответа на задание "Заполните пропуски"
function checkAnswer() {
    const blanks = document.querySelectorAll('.blank');
    const input = document.getElementById('input-answer').value.trim();
    let isCorrect = false;

    blanks.forEach(blank => {
        const correctAnswer = blank.getAttribute('data-answer');
        if (input.toLowerCase() === correctAnswer.toLowerCase()) {
            blank.textContent = input;
            blank.classList.add('filled');
            isCorrect = true;
        }
    });

    const feedback = document.getElementById('feedback');
    if (isCorrect) {
        feedback.textContent = "Правильно!";
        feedback.style.color = "green";
    } else {
        feedback.textContent = "Неправильно. Попробуйте снова.";
        feedback.style.color = "red";
    }
}

// Проверка выбора правильного варианта
function selectOption(button) {
    const selectedAnswer = button.getAttribute('data-answer');
    const feedback = document.getElementById('feedback-choice');

    if (selectedAnswer === "тенге") {
        feedback.textContent = "Правильно!";
        feedback.style.color = "green";
    } else {
        feedback.textContent = "Неправильно. Попробуйте снова.";
        feedback.style.color = "red";
    }
}



// Данные о заданиях
const sections = {
    grammar: {
        title: "Грамматика",
        tasks: [
            {
                type: "fill-in-the-blank",
                question: 'Мен сабаққа <span class="blank" data-answer="барамын">    </span>.',
            },
            {
                type: "fill-in-the-blank",
                question: 'Қазақстанның Ел ордасы — <span class="blank" data-answer="Астана">   </span>.',
            },
            {
                type: "fill-in-the-blank",
                question: 'Бүгін өзімді <span class="blank" data-answer="нашар"> сезініп тұрмын. — </span>.',
            },

        ],
    },
    vocabulary: {
        title: "Словарь",
        tasks: [
            {
                type: "choose",
                question: "Национальная валюта Казахстана — это:",
                options: ["Тенге", "Сом", "Рубль"],
                correct: "Тенге",
            },
        ],
    },
    culture: {
        title: "Культура",
        tasks: [
            {
                type: "fill-in-the-blank",
                question: "Казахское национальное блюдо — <span class='blank' data-answer='бешбармак'>_____</span>.",
            },
        ],
    },
};

// Показать задания раздела
function showTasks(section) {
    const tasksContainer = document.getElementById("tasks-container");
    const tasksContent = document.getElementById("tasks-content");
    const sectionTitle = document.getElementById("section-title");

    // Очистка содержимого
    tasksContent.innerHTML = "";

    // Установка заголовка раздела
    sectionTitle.innerText = sections[section].title;

    // Добавление заданий
    sections[section].tasks.forEach((task, index) => {
        const taskDiv = document.createElement("div");
        taskDiv.classList.add("task");

        if (task.type === "fill-in-the-blank") {
            taskDiv.innerHTML = `<p>${task.question}</p>
                <input type="text" placeholder="Ваш ответ">
                <button onclick="checkAnswer(this, '${task.type}')">Проверить</button>`;
        } else if (task.type === "choose") {
            taskDiv.innerHTML = `<p>${task.question}</p>`;
            task.options.forEach((option) => {
                taskDiv.innerHTML += `<button class="option" onclick="checkAnswer(this, '${task.type}', '${option}', '${task.correct}')">${option}</button>`;
            });
        }

        tasksContent.appendChild(taskDiv);
    });

    // Показать секцию заданий
    tasksContainer.style.display = "block";

    // Скрыть секцию с разделами
    document.querySelector(".section-links").style.display = "none";
}

// Проверить ответ
function checkAnswer(element, type, selectedOption = "", correctAnswer = "") {
    if (type === "fill-in-the-blank") {
        const input = element.previousElementSibling;
        const correct = input.parentElement.querySelector(".blank").dataset.answer;

        if (input.value.trim() === correct) {
            alert("Right!");
        } else {
            alert("False, try again!.");
        }
    } else if (type === "choose") {
        if (selectedOption === correctAnswer) {
            alert("Right!");
        } else {
            alert("False, try again.");
        }
    }
}

// Вернуться к выбору разделов
function goBack() {
    document.getElementById("tasks-container").style.display = "none";
    document.querySelector(".section-links").style.display = "block";
}



