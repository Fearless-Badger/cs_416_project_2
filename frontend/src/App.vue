<template>
  <div id="app">

    <h1>Class Management Interface</h1>

    <!-- MUST DO 
     2. Display average score of students
    -->

    <div id="section-01">
      <div class="form-container">
        <strong>Average Score:</strong> {{averageScore}}
      </div>
    </div>

    <div id="section-02">
      <div class="form-container">
        <input v-model="newStudent.fname" placeholder="First Name" />
        <input v-model="newStudent.mname" placeholder="Middle Name" />
        <input v-model="newStudent.lname" placeholder="Last Name" />
        <input v-model.number="newStudent.score" placeholder="Score" type="number" />
        <input v-model.number="newStudent.student_id" placeholder="Student ID" type="number" />
      </div>

      <button class="list-button button" @click="fetchStudents">Get Students</button>
      <button class="create-button button" @click="addStudent">Add Student</button>


      <table class="students-container">
        <thead>
          <tr>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Last Name</th>
            <th>Score</th>
            <th>Student-id</th>
          </tr>
        </thead>

        <tbody class="student-table" v-for="student in students" :key="student.student_id">

          <tr class="student-card">
            <td>{{ student.fname }}</td>
            <td>{{ student.mname }}</td>
            <td>{{ student.lname }}</td>
            <td>{{ student.score }}</td>
            <td>{{ student.student_id }}</td>

            <td>
              <button @click="updateStudent(student)">Update</button>
            </td>
            <td>
              <button @click="deleteStudent({ 'student_id': student.student_id })">Delete</button>
            </td>

          </tr>

        </tbody>


      </table>

      <div v-if="showEditModal" class="modal-overlay">
        <div class="modal-content">

          <h2>Edit student</h2>

          <label>First Name:</label>
          <input v-model="selectedStudent.fname" />

          <label>Middle Name:</label>
          <input v-model="selectedStudent.mname" />

          <label>Last Name:</label>
          <input v-model="selectedStudent.lname" />

          <label>Score:</label>
          <input type="number" v-model.number="selectedStudent.score" />

          <div class="modal-actions">
            <button @click="submitEdit">Submit</button>
            <button @click="closeModal">Cancel</button>
          </div>
        </div>

      </div>

    </div>





  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      showEditModal: false,
      selectedStudent: null,
      students: [],
      newStudent: {
        fname: '',
        mname: '',
        lname: '',
        score: null,
        student_id: null
      }
    }
  },
  computed: {
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
    async submitEdit() {
      try{
        const response = await fetch('/api/update_student', {
          method : "POST",
          headers: {'Content-Type' : 'application/json'},
          body: JSON.stringify(this.selectedStudent)
        });

        const result = await response.json();
        alert(result.message);

        if (result.result) {
          this.closeModal();
          this.fetchStudents();
        }

      } catch (error) {
        console.error('Update error: ', error);
        alert('Something went wrong while updating.')
      }
    },
    updateStudent(student) {
      this.selectedStudent = { ...student }
      this.showEditModal = true
    },
    closeModal() {
      this.showEditModal = false
      this.selectedStudent = null
    },
    async fetchStudents() {
      try {
        const response = await fetch("/api/list_all");
        const data = await response.json();
        this.students = data;
      } catch (error) {
        console.error("ERROR (U messed up lil bro): ", error);
      }
    },
    async deleteStudent(id_json) {
      try {
        const response = await fetch('/api/delete_student', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(id_json)
        });
        let message;
        if (response.ok) {
          message = "Student Removed";
          this.fetchStudents();
        } else {
          message = "Not ok...";
        }
        alert(message);
      } catch (shameful_mistake) {
        console.error("ERROR (Just prompt the AI lil bro): ", shameful_mistake);
      }
    },
    async addStudent() {
      try {
        const response = await fetch('/api/add_student', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newStudent),
        });

        const result = await response.json();

        alert(result.message);

        if (result.result) {
          this.fetchStudents(); // Refresh the list
          this.newStudent = { fname: '', mname: '', lname: '', score: null, student_id: null }; // Clear form
        }

      } catch (error) {
        console.error("Add Student Error:", error);
        alert("Something went wrong. Please try again.");
      }
    }
  }
}
</script>

<style>
/* Alternate box model (box model suxx) */
*,
*:before,
*:after {
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

.student {
  list-style-type: none;
}

.students-container {
  border: 2px solid black;
}

.button {
  color: #2c3e50;
  background-color: lightgreen;
  padding: 5px 10px;
  border: none;
  border-radius: 10%;
  cursor: pointer;
  margin: 10px;
}
</style>
