<template>
  <div v-if="isAuthenticated" class="group-list">
    <div class="mb-4 flex justify-center space-x-4">
      <button 
        @click="setView('myGroups')" 
        class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-500 transition duration-300"
      >
        View My Groups
      </button>
      <button 
        @click="setView('joinGroups')" 
        class="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-500 transition duration-300"
      >
        Join a Group
      </button>
      <button 
        @click="setView('createGroup')" 
        class="bg-gray-600 text-white py-2 px-4 rounded hover:bg-gray-500 transition duration-300"
      >
        Create a Group
      </button>
    </div>

    <div class="mb-4 flex justify-center space-x-4">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search for a group"
        class="border border-gray-300 rounded-lg p-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        @click="searchGroups"
        class="bg-indigo-600 text-white py-2 px-4 rounded hover:bg-indigo-500 transition duration-300"
      >
        Search
      </button>
    </div>

    <div v-if="currentView === 'myGroups'">
      <h2 class="text-2xl font-semibold mb-4">My Groups</h2>
      <ul v-if="groups.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <li v-for="group in groups" :key="group.id" class="bg-white rounded-lg shadow p-4">
          <h3 class="text-lg font-bold">{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></h3>
          <p class="text-gray-700">{{ group.description }}</p>
  
          <h4 class="font-semibold mt-2">Members:</h4>
          <ul v-if="group.members && group.members.length > 0">
            <span v-for="(member, index) in group.members" :key="member.id">
              {{ member.username }}{{ index === group.members.length - 1 ? '.' : ', ' }}
            </span>
          </ul>
          <p v-else class="text-gray-500">No members yet.</p>
  
          <button 
            @click="leaveGroup(group.id)" 
            class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500 transition duration-300"
          >
            Leave Group
          </button>
        </li>
      </ul>
      <p v-else class="text-center">No groups available yet.</p>
    </div>

    <div v-if="currentView === 'joinGroups'">
      <h2 class="text-2xl font-semibold mb-4">Groups</h2>
      <ul v-if="availableGroups.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <li v-for="group in availableGroups" :key="group.id" class="bg-white rounded-lg shadow p-4">
          <h3 class="text-lg font-bold">{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></h3>
          <p>{{ group.description }}</p>
  
          <h4 class="font-semibold mt-2">Members:</h4>
          <ul v-if="group.members && group.members.length > 0">
            <span v-for="(member, index) in group.members" :key="member.id">
              {{ member.username }}{{ index === group.members.length - 1 ? '.' : ', ' }}
            </span>
          </ul>
          <p v-else>No members yet.</p>
  
          <button 
            @click="joinGroup(group.id)" 
            class="mt-2 bg-green-600 text-white py-1 px-4 rounded hover:bg-green-500 transition duration-300"
          >
            Join
          </button>
        </li>
      </ul>
      <p v-else>No groups available yet.</p>
    </div>

    <div v-if="currentView === 'createGroup'">
      <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
        <h2 class="text-2xl font-semibold mb-4 text-center">Create Group</h2>
        <form @submit.prevent="createGroup" class="space-y-4">
          <div>
            <input 
              v-model="name" 
              type="text" 
              placeholder="Group Name" 
              class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>
          <div>
            <textarea 
              v-model="description" 
              placeholder="Group Description" 
              class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            ></textarea>
          </div>
          <div>
            <label for="isPublic" class="block mb-2">Group Privacy:</label>
            <select v-model="isPublic" class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500">
              <option :value="true">Public</option>
              <option :value="false">Private</option>
            </select>
          </div>
          <button 
            type="submit"
            class="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-500 transition duration-200"
          >
            Create Group
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';
import { computed } from 'vue';
import { useToast } from 'vue-toastification';

export default {
  setup() {
    const store = useStore();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    return { isAuthenticated };
  },
  data() {
    return {
      groups: [],
      availableGroups: [],
      name: '',
      description: '',
      isPublic: true,
      currentView: 'myGroups',
      searchQuery: ''
    };
  },
  mounted() {
    this.fetchUserGroups();
    this.toast = useToast();
  },
  methods: {
    setView(view) {
      this.currentView = view;
      if (view === 'joinGroups') {
        this.fetchAvailableGroups();
      }
    },
    fetchUserGroups() {
      axios.get('/groups/mine')
        .then(response => {
          this.groups = response.data;
        })
        .catch(error => {
          console.error('Error fetching user groups:', error);
        });
    },
    fetchAvailableGroups() {
      axios.get('/groups/not-mine')
        .then(response => {
          this.availableGroups = response.data;
        })
        .catch(error => {
          console.error('Error fetching available groups:', error);
        });
    },
    joinGroup(groupId) {
      axios.post(`/groups/join/${groupId}`)
        .then(response => {
          this.toast.success(response.data.message);
          const joinedGroup = this.availableGroups.find(group => group.id === groupId);
          if (joinedGroup) {
            this.groups.push(joinedGroup);
            this.availableGroups = this.availableGroups.filter(group => group.id !== groupId);
          }
         })
         .catch(error => {
          this.toast.error('An error occurred while joining the group.');
          console.error('Error joining group:', error);
        });
    },
    leaveGroup(groupId) {
      axios.post(`/groups/leave/${groupId}`)
        .then(response => {
          this.toast.success(response.data.message);
          this.fetchUserGroups();
        })
        .catch(error => {
          this.toast.error('An error occurred while leaving the group.');
          console.log('Error leaving group:', error);
        });
    },
    createGroup() {
      if (!this.description) {
        this.description = `${this.$store.state.user.username}'s ${this.isPublic ? 'public' : 'private'} group`;
      }
      
      axios.post('/groups', {
        name: this.name,
        description: this.description,
        is_public: this.isPublic
      })
      .then(() => {
        this.toast.success('Group created successfully!');
        this.name = '';
        this.description = '';
        this.isPublic = true;
        this.fetchUserGroups();
        this.setView('myGroups');
      })
      .catch(error => {
        this.toast.error('An error occurred while creating the group.');
        console.error('Error creating group:', error);
      });
    },
    searchGroups() {
      if(this.searchQuery.trim() === '') {
        axios.get('/groups/not-mine')
          .then(response => {
            this.availableGroups = response.data;
          })
          .catch(error => {
            console.error('Error searching groups:', error);
        });
      } else {
          axios.get(`/groups/search?query=${this.searchQuery}`)
          .then(response => {
            this.availableGroups = response.data;
            this.currentView = 'joinGroups';
          })
          .catch(error => {
            console.error('Error searching groups:', error);
          });
      }
    }
  },
};
</script>

<style scoped>
.group-list {
  max-width: 800px;
  margin: 0 auto;
}
</style>

