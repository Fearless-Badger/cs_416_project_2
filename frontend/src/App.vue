<template>
    <div id="app">

    <h1>Class Management Interface</h1>

    <!-- MUST DO 
    2. Display average score of students
    -->

    <div id="section-01">
      <!-- 2. Display average score of students -->
    </div>

    <div id="section-02">
      <div class="form-container">
        <input v-model="newStudent.fname" placeholder="First Name" />
        <input v-model="newStudent.mname" placeholder="Middle Name" />
        <input v-model="newStudent.lname" placeholder="Last Name" />
        <input v-model.number="newStudent.score" placeholder="Score" type="number" />
        <input v-model.number="newStudent.student_id" placeholder="Student ID" type="number" />
        <button class="create-button button" @click="addStudent">Add Student</button>
      </div>


      <table class="students-container">
        <thead>
          <tr>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Last Name</th>
            <th>Score</th>
            <th>Student-id</th>
            <th><button class="list-button button" @click="fetchStudents">Refresh Listing</button></th>
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
              <button class="update-button button" @click="updateStudent(student)">Update</button>
              <button class="delete-button button" @click="deleteStudent({ 'student_id': student.student_id })">Delete</button>
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

.update-button,
.delete-button {
  margin: 4px 8px;
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

.delete-button{
  background-color: rgb(201, 89, 89);
  color: white;
}

.list-button {
  margin-left: 16px;
}

</style>
