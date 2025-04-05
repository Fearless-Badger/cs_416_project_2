<template>
  <div id="app">
    <main class="main-content">
      <h1>📚 Class Management Interface</h1>

    <!-- Average Score -->
    <div id="section-01" v-if="students.length">
      <h2 class="average-score">Average Score: {{ averageScore }}</h2>

    </div>

    <!-- Student Input & Table -->
    <div id="section-02">
      <div class="form-container">
        <input v-model="newStudent.fname" placeholder="First Name" />
        <input v-model="newStudent.mname" placeholder="Middle Name" />
        <input v-model="newStudent.lname" placeholder="Last Name" />
        <input v-model.number="newStudent.score" placeholder="Score" type="number" />
        <input v-model.number="newStudent.student_id" placeholder="Student ID" type="number" />
        <button class="create-button button" @click="addStudent">Add Student</button>
      </div>

        <div class="button-group">
          <button class="list-button button" @click="fetchStudents">Refresh Students</button>
        </div>

        <table class="students-container" v-if="students.length">
          <thead>
            <tr>
              <th>First</th>
              <th>Middle</th>
              <th>Last</th>
              <th>Score</th>
              <th>ID</th>
              <th colspan="2">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="student in sortedStudents" :key="student.student_id">
              <td>{{ student.fname }}</td>
              <td>{{ student.mname }}</td>
              <td>{{ student.lname }}</td>
              <td>{{ student.score }}</td>
              <td>{{ student.student_id }}</td>
              <td><button @click="updateStudent(student)">✏️</button></td>
              <td><button class="delete-button" @click="deleteStudent({ student_id: student.student_id })">🗑️</button></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Edit Modal -->
      <div v-if="showEditModal" class="modal-overlay">
        <div class="modal-content">
          <h2>Edit Student</h2>
          <label>First Name:</label>
          <input v-model="selectedStudent.fname" />
          <label>Middle Name:</label>
          <input v-model="selectedStudent.mname" />
          <label>Last Name:</label>
          <input v-model="selectedStudent.lname" />
          <label>Score:</label>
          <input type="number" v-model.number="selectedStudent.score" />

          <div class="modal-actions">
            <button @click="submitEdit">Save</button>
            <button @click="closeModal">Cancel</button>
          </div>
        </div>
      </div>
    </main>

    <!-- FOOTER -->
    <footer class="app-footer">
      <p>
        View the project on
        <a href="https://github.com/Fearless-Badger/cs_416_project_2" target="_blank">Github</a>
        |
        View the frontend Image on
        <a href="https://hub.docker.com/r/badger54/cs_416_project" target="_blank">Docker Hub</a>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      students: [],
      newStudent: {
        fname: '',
        mname: '',
        lname: '',
        score: null,
        student_id: null
      },
      selectedStudent: null,
      showEditModal: false
    }
  },
  computed: {
    sortedStudents() {
      return [...this.students].sort((a, b) => { 
      if (a.score !== b.score) {
	return b.score - a.score;
	}
	return a.fname.localeCompare(b.fname);
    });
  },
    averageScore() { 
      if (!this.students.length) return 0;
      let total = 0;
      for(let student of this.students) {
        total += student.score;
      }
      return (total / this.students.length).toFixed(2);
    }
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await fetch("/api/list_all");
        this.students = await response.json();
      } catch (error) {
        console.error("Fetch error:", error);
      }
    },
    async addStudent() {
      try {
        const response = await fetch("/api/add_student", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.newStudent),
        });
        const result = await response.json();
        alert(result.message);
        if (result.result === "True") {
          this.fetchStudents();
          this.newStudent = { fname: '', mname: '', lname: '', score: null, student_id: null };
        }
        this.fetchStudents()
      } catch (error) {
        console.error("Add error:", error);
        alert("Something went wrong. Try again.");
      }
    },
    async deleteStudent(id_json) {
      try {
        const response = await fetch("/api/delete_student", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(id_json),
        });
        if (response.ok) {
          alert("Student deleted ✅");
          this.fetchStudents();
        } else {
          alert("Failed to delete student ❌");
        }
      } catch (error) {
        console.error("Delete error:", error);
      }
    },
    updateStudent(student) {
      this.selectedStudent = { ...student }
      this.showEditModal = true
    },
    closeModal() {
      this.selectedStudent = null
      this.showEditModal = false
    },
    async submitEdit() {
      try {
        const response = await fetch("/api/update_student", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.selectedStudent)
        });
        const result = await response.json();
        alert(result.message);
        if (result.result) {
          this.closeModal();
          this.fetchStudents();
        }
      } catch (error) {
        console.error("Edit error:", error);
      }
    }
  },
  mounted() {
    this.fetchStudents();
  }
}
</script>

<style>
*,
*:before,
*:after {
  box-sizing: border-box;
}

body {
  background-color: #f8f8fc;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.average-score {
  font-size: 20px;
  font-weight: bold;
  color: #009688;
  margin-bottom: 20px;
}

.form-container input {
  margin: 5px;
  padding: 8px;
  border-radius: 8px;
  border: 1px solid #ccc;
  width: 150px;
}

.button-group {
  margin-top: 10px;
}

.button {
  background-color: #4CAF50;
  color: white;
  padding: 7px 15px;
  margin: 5px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.delete-button {
  background-color: #e74c3c;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.update-button,
.delete-button {
  margin: 4px 8px;
}


.students-container {
  width: 100%;
  max-width: 800px;
  margin: 20px auto;
  border-collapse: collapse;
}

.students-container th,
.students-container td {
  padding: 10px;
  border: 1px solid #ddd;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 25px;
  border-radius: 10px;
  width: 300px;
  text-align: left;
}

.modal-content label {
  display: block;
  margin: 10px 0 5px;
}

.modal-content input {
  width: 100%;
  padding: 5px;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.delete-button{
  background-color: rgb(201, 89, 89);
  color: white;
}

.list-button {
  margin-left: 16px;
}

/* Footer Styling */
.app-footer {
  background-color: #2c3e50;
  color: white;
  padding: 10px;
  text-align: center;
}
.app-footer a {
  color: rgb(112, 155, 158);
  text-decoration: none;
  margin: 0 5px;
  
}
.app-footer a:hover {
  text-decoration: underline;
}

</style>