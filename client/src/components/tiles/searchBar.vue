<template>
  <div>
    <input type="text" v-model="searchQuery" placeholder="Search...">
    <ul>
      <li v-for="item in filteredList" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { id: 1, name: 'Item 1' },
        { id: 2, name: 'Item 2' },
        { id: 3, name: 'Item 3' },
      ],
      searchQuery: ''
    };
  },
  computed: {
    filteredList() {
      const query = this.searchQuery.toLowerCase();
      return this.items.filter(item => item.name.toLowerCase().includes(query));
    }
  }
};
</script>
