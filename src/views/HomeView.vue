<template>
  <div>
    <table class="database-output">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Summary</th>
          <th>Category</th>
          <th>Number of Pages</th>
          <th>Rating</th>
          <th>Author Name</th>
          <th>Author Lastname</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book[0]">
          <td>{{ book[0] }}</td>
          <td>{{ book[1] }}</td>
          <td>{{ book[2] }}</td>
          <td>{{ book[3] }}</td>
          <td>{{ book[4] }}</td>
          <td>{{ book[5] }}</td>
          <td>{{ book[6] }}</td>
          <td>{{ book[7] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books : []
    }
  },
  created() {
      const socket = new WebSocket('ws://localhost:12345')
      socket.addEventListener('message', (event) => {
      const data = JSON.parse(event.data)
      this.books = data
      console.log(this.books)
    })
  },
  mounted() {
    console.log('Hello World!')
  }
}
</script>
