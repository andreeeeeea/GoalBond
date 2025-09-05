<template>
  <div class="overflow-x-auto bg-gray-100 min-h-screen">
    <div class="container mx-auto p-4">
      <!-- Top Section with Title -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-800">Account Settings</h1>
        <p class="text-gray-600">Manage your account preferences and groups</p>
      </div>

      <!-- Main Content Card -->
      <div class="bg-white rounded-lg shadow-lg p-6">
        <!-- Tab Navigation -->
        <div class="flex space-x-4 mb-6 border-b">
          <button 
            v-for="tab in ['account', 'myGroups', 'joinGroups', 'createGroup']" 
            :key="tab"
            @click="setView(tab)"
            :class="[
              'px-4 py-2 font-medium transition-colors duration-200',
              currentView === tab 
                ? 'text-blue-600 border-b-2 border-blue-600' 
                : 'text-gray-600 hover:text-blue-600'
            ]"
          >
            {{ formatTabName(tab) }}
          </button>
        </div>

        <!-- Content Sections -->
        <div class="mt-6">
          <!-- Account Section -->
          <div v-if="currentView === 'account'" class="space-y-6">
            <div v-if="!editing" class="space-y-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-gray-50 rounded-lg">
                  <p class="text-sm text-gray-600">Nickname</p>
                  <p class="text-lg font-medium">{{ nickname }}</p>
                </div>
                <div class="p-4 bg-gray-50 rounded-lg">
                  <p class="text-sm text-gray-600">Username</p>
                  <p class="text-lg font-medium">{{ username }}</p>
                </div>
                <div class="p-4 bg-gray-50 rounded-lg">
                  <p class="text-sm text-gray-600">Email</p>
                  <p class="text-lg font-medium">{{ email }}</p>
                </div>
              </div>
              
              <div class="flex space-x-4">
                <button
                  @click="startEdit"
                  class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Edit Profile
                </button>
                <button
                  @click="logout"
                  class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
                >
                  Logout
                </button>
              </div>
            </div>

            <!-- Edit Form -->
            <div v-else class="space-y-4">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">Nickname</label>
                  <input
                    v-model="form.nickname"
                    type="text"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">Username</label>
                  <input
                    v-model="form.username"
                    type="text"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">Email</label>
                  <input
                    v-model="form.email"
                    type="email"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div class="space-y-4">
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">Current Password</label>
                  <input
                    v-model="form.oldPassword"
                    type="password"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">New Password</label>
                  <input
                    v-model="form.newPassword"
                    type="password"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-medium text-gray-700">Confirm New Password</label>
                  <input
                    v-model="form.confirmPassword"
                    type="password"
                    class="w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div class="flex space-x-4">
                <button
                  @click="updateAccount"
                  class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
                >
                  Save Changes
                </button>
                <button
                  @click="cancelEdit"
                  class="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors"
                >
                  Cancel
                </button>
              </div>

              <div class="mt-8 pt-4 border-t">
                <button
                  @click="deleteAccount"
                  class="px-4 py-2 bg-red-100 text-red-700 rounded-lg hover:bg-red-200 transition-colors"
                >
                  Delete Account
                </button>
                <p class="mt-2 text-sm text-red-600">Warning: This action cannot be undone.</p>
              </div>
            </div>
          </div>

      <!-- My Groups Section -->
      <div v-if="currentView === 'myGroups'">
        <h2 class="text-2xl font-semibold mb-4">My Groups</h2>
        <ul v-if="groups.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <li v-for="group in groups" :key="group.id" class="bg-white rounded-lg border-solid border-2  p-4">
            <div class="flex flex-col justify-between h-full">
              <div>
                <div class="block text-md text-gray-700"><strong>{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></strong></div>
                <div class="block text-md text-gray-700"><strong>Owner</strong>: {{ group.owner.username }}</div>
                <div class="block text-md text-gray-700">{{ group.members.length }} members.</div>
                <div v-if="group.description" class="block text-md text-gray-700">"{{ group.description }}"</div>
              </div>
              <button
                @click="leaveGroup(group.id)"
                class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500"
              >
                Leave Group
              </button>
              <div v-if="group.owner.id === currentUser.id">
                <button
                  @click="deleteGroup(group.id)"
                  class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500"
                >
                  Delete Group
                </button>
              </div>
            </div>
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
        <ul v-if="availableGroups.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
          <li v-for="group in availableGroups" :key="group.id" class="bg-white rounded-lg shadow p-4">
            <div class="flex flex-col justify-between h-full">
              <div>
                <div class="block text-md text-gray-700"><strong>{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></strong></div>
                <div class="block text-md text-gray-700"><strong>Owner</strong>: {{ group.owner.username }}</div>
                <div class="block text-md text-gray-700">{{ group.members.length }} members.</div>
                <div v-if="group.description" class="block text-md text-gray-700">"{{ group.description }}"</div>
              </div>
              <button
                v-if="group.members.find(member => member.id === currentUser.id)"
                @click="leaveGroup(group.id)"
                class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500"
              >
                Leave
              </button>
              <button
                v-else
                @click="joinGroup(group.id)"
                class="mt-4 bg-green-600 text-white py-1 px-4 rounded hover:bg-green-500"
              >
                Join
              </button>
            </div>
          </li>
        </ul>
        <p v-else>No groups available yet.</p>
      </div>

      <!-- Create Group Section -->
      <div v-if="currentView === 'createGroup'" class="max-w-md">
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
    </div>
  </div>
</template>


<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  setup() {
    const toast = useToast();

    return {
      toast,
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
      owner: '',
      availableGroups: [],
      name: '',
      description: '',
      isPublic: true,
      publicGroups: [],
      searchQuery: '',
      form: {
        nickname: this.getNickname,
        username: this.getUsername,
        email: this.getEmail,
        oldPassword: '',
        newPassword: '',
        confirmPassword: '',
      },
      editing: false,
    };
  },
  mounted() {
    this.toast = useToast();
    this.fetchUserGroups();
    this.fetchPublicGroups();
  },
  methods: {
    async logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
      this.toast.success('You have logged out successfully.');
    },
    
    setView(view) {
      this.currentView = view;
      if (view === 'joinGroups') this.fetchAvailableGroups();
    },
    getTabClass(view) {
    return this.currentView === view
      ? 'tab active'
      : 'tab text-gray-600'; 
    },
    startEdit() {
      this.editing = true; 
    },
    cancelEdit() {
      this.editing = false; 
    },
    async updateAccount() {
      try {
        const updatedFields = {};

        if (this.form.oldPassword) {
          const passwordMatchResponse = await axios.post('/check-password', {
            password: this.form.oldPassword  // This should be sent as 'password'
          });

          if (passwordMatchResponse.status !== 200) {
            this.toast.error('Old password is incorrect.');
            return;
          }
        }

        if (this.form.newPassword !== this.form.confirmPassword) {
          this.toast.error('New passwords do not match.');
          return;
        }

        if (this.form.nickname !== this.getNickname) {
          updatedFields.nickname = this.form.nickname;
        }
        if (this.form.username !== this.getUsername) {
          updatedFields.username = this.form.username;
        }
        if (this.form.email !== this.getEmail) {
          updatedFields.email = this.form.email;
        }
        if (this.form.newPassword) {
          updatedFields.password = this.form.newPassword;
        }

        const response = await axios.put('/update-user', updatedFields);
        
        console.log('Account updated:', response.data);
        this.toast.success('Account updated successfully.');
        this.editing = false; 
      } catch (error) {
        console.error('Error updating account:', error); 
        this.toast.error('An error occurred while updating the account');
      }
    },
    async deleteAccount() {
      if (confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
        try {
          const response = await axios.delete('/delete_account');
          if (response.data.success) {
            alert(response.data.message); 
            window.location.href = "/";  
          } else {
            console.log('Error deleting account:', response.data.message);
            this.toast.error('Failed to delete account. Please try again.');
          }
        } catch (error) {
          console.error("Error deleting account:", error);
          this.toast.error('Failed to delete account. Please try again.');
        }
      }
    },
    async fetchUserGroups() {
      try {
        const response = await axios.get('/groups/mine');
        this.groups = response.data;
      } catch (error) {
        if (error.response?.status === 401) {
          this.groups = [];
        } else {
          console.log('Error fetching user groups:', error);
        }
      }
    },
    async fetchPublicGroups() {
      try {
        const response = await axios.get('/groups');
        this.publicGroups = response.data.filter(
          (group) => group.is_public && group.members.some((member) => member.username === this.username)
        );
      } catch (error) {
        if(error.response?.status === 401) {
          this.publicGroups = [];
        } else {
          console.error('Error fetching public groups:', error);
        }
      }
    },
    async fetchAvailableGroups() {
      try {
        const response = await axios.get('/groups/not-mine');
        this.availableGroups = response.data;
      } catch (error) {
        if (error.response?.status === 401) {
          this.availableGroups = [];
        } else {
          console.error('Error fetching available groups:', error);
        }
      }
    },
    async createGroup() {
      try {
        await axios.post('/groups', { name: this.name, description: this.description, is_public: this.isPublic });
        this.toast.success('Group created successfully!');
        this.name = '';
        this.description = '';
        this.isPublic = true;
        this.fetchUserGroups();
      } catch (error) {
        this.toast.error('Error creating group. Please try again.');
      }
    },
    async joinGroup(groupId) {
      try {
        await axios.post(`/groups/join/${groupId}`);
        this.toast.success('You have joined the group!');
        this.fetchUserGroups();
        this.fetchAvailableGroups();
      } catch (error) {
        this.toast.error('Error joining group. Please try again.');
      }
    },
    async leaveGroup(groupId) {
      try {
        const response = await axios.post(`/groups/${groupId}/leave`);
        
        if (response.data.message.includes('the group has been deleted')){
          this.toast.success(response.data.message);
          this.groups = this.groups.filter(group => group.id !== groupId);
        } else {
          this.toast.success('You have left the group!');
          this.groups.find(group => group.id === groupId).members = this.groups.find(group => group.id === groupId).members.filter(member => member.username !== this.username);
        }
      } catch (error) {
        this.toast.error('Error leaving group. Please try again.');
      }
    },
    async searchGroups() {
      try {
        const response = await axios.get(`/groups/search?query=${this.searchQuery}`);
        this.availableGroups = response.data;
      } catch (error) {
        this.toast.error('Error searching groups. Please try again.');
      }
    },
    async deleteGroup(groupId) {
      try {
        await axios.delete(`/groups/${groupId}`);
        this.toast.success('Group deleted successfully!');
        this.fetchUserGroups();
        this.fetchAvailableGroups();
      } catch (error) {
        this.toast.error('Error deleting group. Please try again.');
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
.success {
  color: green;
}
.error {
  color: red;
}
</style>

