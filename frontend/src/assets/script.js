// Store students data
let students = [];

// Function to add student data
function addStudent(event) {
    event.preventDefault();

    const firstName = document.getElementById('first-name').value;
    const middleName = document.getElementById('middle-name').value;
    const lastName = document.getElementById('last-name').value;
    const studentId = document.getElementById('student-id').value;
    const score = parseInt(document.getElementById('score').value);

    // Create student object
    const student = {
        firstName,
        middleName,
        lastName,
        studentId: parseInt(studentId),
        score
    };

    // Add student to array
    students.push(student);

    // Clear the form fields
    document.getElementById('student-form').reset();

    // Update the table and average score
    updateTable();
    updateAverageScore();
}

// Function to update the table
function updateTable() {
    const tbody = document.querySelector('#student-table tbody');
    tbody.innerHTML = '';

    // Sort students by score in ascending order
    students.sort((a, b) => a.score - b.score);

    // Populate the table with student data
    students.forEach(student => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${student.firstName} ${student.middleName} ${student.lastName}</td>
            <td>${student.studentId}</td>
            <td>${student.score}</td>
        `;
        tbody.appendChild(row);
    });
}

// Function to update the average score
function updateAverageScore() {
    if (students.length === 0) {
        document.getElementById('average-score').innerText = '0';
        return;
    }

    const totalScore = students.reduce((acc, student) => acc + student.score, 0);
    const averageScore = totalScore / students.length;
    document.getElementById('average-score').innerText = averageScore.toFixed(2);
}

// Add event listener for form submission
document.getElementById('student-form').addEventListener('submit', addStudent);
