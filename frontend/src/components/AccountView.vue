<template>
  <div class="container mx-auto">
    <div class="flex items-center my-11">
      <div class="rounded-full bg-gray-300 w-32 h-32 mr-4"></div>
      <div class="flex flex-col">
        <span class="text-3xl font-bold"> {{ nickname }}</span>
        <span class="text-lg">{{ username }}</span>
      </div>
    </div>
  </div>

  <div class="container mx-auto">
    <!-- Tab Navigation -->
    <div class="flex justify-left mb-8 space-x-5">
      <div
        @click="setView('account')"
        :class="getTabClass('account')"
        class="tab"
      >
        Account
      </div>
      <div
        @click="setView('myGroups')"
        :class="getTabClass('myGroups')"
        class="tab"
      >
        My Groups
      </div>
      <div
        @click="setView('joinGroups')"
        :class="getTabClass('joinGroups')"
        class="tab"
      >
        Join a Group
      </div>
      <div
        @click="setView('createGroup')"
        :class="getTabClass('createGroup')"
        class="tab"
      >
        Create a Group
      </div>
    </div>

    <!-- Account Section -->
    <div v-if="currentView === 'account'" class="flex flex-col">
      <h2 class="text-2xl font-bold mb-5">Account Information</h2>

      <div class="block text-xl text-gray-700"><strong>Nickname:</strong> {{ nickname }}</div>
      <div class="block text-xl text-gray-700"><strong>Username:</strong> {{ username }}</div>
      <div class="block text-xl text-gray-700"><strong>Email:</strong> {{ email }}</div>

      <!-- Logout Button -->
       <div class="flex flex-row space-x-6 mt-5">
        <button
          @click="logout"
          class="text-white w-40 bg-red-600 hover:bg-red-700 px-4 py-2 rounded mt-2"
        >
          Logout
        </button>
        <button
          class="text-white w-40 bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded mt-2"
        >
          Edit Account
        </button>
       </div>

    </div>






    <!-- My Groups Section -->
    <div v-if="currentView === 'myGroups'">
      <h2 class="text-2xl font-semibold mb-4">My Groups</h2>
      <ul v-if="groups.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <li v-for="group in groups" :key="group.id" class="bg-white rounded-lg shadow p-4">
          <h3 class="text-lg font-bold">{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></h3>
          <p>{{ group.description }}</p>
          <button
            @click="leaveGroup(group.id)"
            class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500"
          >
            Leave Group
          </button>
        </li>
      </ul>
      <p v-else>No groups available yet.</p>
    </div>

    <!-- Join Groups Section -->
    <div v-if="currentView === 'joinGroups'">
      <h2 class="text-2xl font-semibold mb-4">Join a Group</h2>
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search for a group"
        class="border border-gray-300 rounded-lg p-2 w-full max-w-md mb-4"
      />
      <button @click="searchGroups" class="bg-indigo-600 text-white py-2 px-4 rounded">
        Search
      </button>
      <ul v-if="availableGroups.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
        <li v-for="group in availableGroups" :key="group.id" class="bg-white rounded-lg shadow p-4">
          <h3 class="text-lg font-bold">{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></h3>
          <p>{{ group.description }}</p>
          <button
            @click="joinGroup(group.id)"
            class="mt-2 bg-green-600 text-white py-1 px-4 rounded"
          >
            Join
          </button>
        </li>
      </ul>
      <p v-else>No groups available yet.</p>
    </div>

    <!-- Create Group Section -->
    <div v-if="currentView === 'createGroup'" class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold mb-4">Create a Group</h2>
      <form @submit.prevent="createGroup">
        <input
          v-model="name"
          type="text"
          placeholder="Group Name"
          class="border border-gray-300 rounded-lg p-2 w-full mb-4"
          required
        />
        <textarea
          v-model="description"
          placeholder="Group Description"
          class="border border-gray-300 rounded-lg p-2 w-full mb-4"
        ></textarea>
        <label class="block mb-2">Group Privacy:</label>
        <select v-model="isPublic" class="border border-gray-300 rounded-lg p-2 w-full mb-4">
          <option :value="true">Public</option>
          <option :value="false">Private</option>
        </select>
        <button type="submit" class="w-full bg-green-600 text-white py-2 rounded-lg">
          Create Group
        </button>
      </form>
    </div>

    <!-- Success and Error Messages -->
    <div v-if="successMessage" class="text-green-500 text-center mt-4">{{ successMessage }}</div>
    <div v-if="errorMessage" class="text-red-500 text-center mt-4">{{ errorMessage }}</div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const logout = async () => {
      await store.dispatch('logout');
      router.push('/login');
    };

    return {
      logout,
    };
  },
  computed: {
    ...mapGetters(['getUsername', 'getEmail', 'getNickname', 'isAuthenticated', 'currentUser']),
    username() {
      return this.getUsername;
    },
    email() {
      return this.getEmail;
    },
    nickname() {
      return this.getNickname;
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    currentUser() {
      return this.$store.getters.currentUser;
    },
  },
  data() {
    return {
      currentView: 'account',
      groups: [],
      availableGroups: [],
      name: '',
      description: '',
      isPublic: true,
      publicGroups: [],
      successMessage: '',
      errorMessage: '',
      searchQuery: '',
    };
  },
  mounted() {
    this.fetchUserGroups();
    this.fetchPublicGroups();
  },
  methods: {
    setView(view) {
      this.currentView = view;
      if (view === 'joinGroups') this.fetchAvailableGroups();
    },
    getButtonClass(view) {
      return `py-2 px-4 rounded ${this.currentView === view ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700'}`;
    },
    getTabClass(view) {
    return this.currentView === view
      ? 'tab active'
      : 'tab text-gray-600'; // Default state for non-active tabs
  },
    async fetchUserGroups() {
      try {
        const response = await axios.get('/groups/mine');
        this.groups = response.data;
      } catch (error) {
        console.error('Error fetching user groups:', error);
      }
    },
    async fetchPublicGroups() {
      try {
        const response = await axios.get('/groups');
        this.publicGroups = response.data.filter(
          (group) => group.is_public && group.members.some((member) => member.username === this.username)
        );
      } catch (error) {
        console.error('Error fetching public groups:', error);
      }
    },
    async fetchAvailableGroups() {
      try {
        const response = await axios.get('/groups/not-mine');
        this.availableGroups = response.data;
      } catch (error) {
        console.error('Error fetching available groups:', error);
      }
    },
    async joinGroup(groupId) {
      try {
        await axios.post(`/groups/join/${groupId}`);
        this.successMessage = 'Successfully joined the group!';
        this.fetchUserGroups();
        this.fetchAvailableGroups();
      } catch (error) {
        this.errorMessage = 'Error joining group.';
      }
    },
    async leaveGroup(groupId) {
      try {
        await axios.post(`/groups/leave/${groupId}`);
        this.successMessage = 'Successfully left the group!';
        this.fetchUserGroups();
      } catch (error) {
        this.errorMessage = 'Error leaving group.';
      }
    },
    async createGroup() {
      try {
        await axios.post('/groups', { name: this.name, description: this.description, is_public: this.isPublic });
        this.successMessage = 'Group created successfully!';
        this.name = '';
        this.description = '';
        this.isPublic = true;
        this.fetchUserGroups();
      } catch (error) {
        this.errorMessage = 'Error creating group.';
      }
    },
    async searchGroups() {
      try {
        const response = await axios.get(`/groups/search?query=${this.searchQuery}`);
        this.availableGroups = response.data;
      } catch (error) {
        this.errorMessage = 'Error searching groups.';
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
