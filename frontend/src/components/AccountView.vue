<template>
  <div class="bg-white shadow-xl rounded-xl w-full sm:w-4/5 md:w-3/4 lg:w-1/2 min-h-96 max-h-auto mx-auto p-5 sm:p-10 md:p-16 my-10 sm:my-16">
    <div class="container mx-auto">
      <div class="flex items-center mb-8 sm:mb-11">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100px" height="100px" viewBox="0 0 20 20" version="1.1">
          <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g id="Dribbble-Light-Preview" transform="translate(-140.000000, -2159.000000)" fill="#000000">
                  <g id="icons" transform="translate(56.000000, 160.000000)">
                      <path d="M100.562548,2016.99998 L87.4381713,2016.99998 C86.7317804,2016.99998 86.2101535,2016.30298 86.4765813,2015.66198 C87.7127655,2012.69798 90.6169306,2010.99998 93.9998492,2010.99998 C97.3837885,2010.99998 100.287954,2012.69798 101.524138,2015.66198 C101.790566,2016.30298 101.268939,2016.99998 100.562548,2016.99998 M89.9166645,2004.99998 C89.9166645,2002.79398 91.7489936,2000.99998 93.9998492,2000.99998 C96.2517256,2000.99998 98.0830339,2002.79398 98.0830339,2004.99998 C98.0830339,2007.20598 96.2517256,2008.99998 93.9998492,2008.99998 C91.7489936,2008.99998 89.9166645,2007.20598 89.9166645,2004.99998 M103.955674,2016.63598 C103.213556,2013.27698 100.892265,2010.79798 97.837022,2009.67298 C99.4560048,2008.39598 100.400241,2006.33098 100.053171,2004.06998 C99.6509769,2001.44698 97.4235996,1999.34798 94.7348224,1999.04198 C91.0232075,1998.61898 87.8750721,2001.44898 87.8750721,2004.99998 C87.8750721,2006.88998 88.7692896,2008.57398 90.1636971,2009.67298 C87.1074334,2010.79798 84.7871636,2013.27698 84.044024,2016.63598 C83.7745338,2017.85698 84.7789973,2018.99998 86.0539717,2018.99998 L101.945727,2018.99998 C103.221722,2018.99998 104.226185,2017.85698 103.955674,2016.63598" id="profile_round-[#1342]"></path>
                  </g>
              </g>
          </g>
      </svg>
        <div class="flex flex-col ml-4 sm:ml-8">
          <span class="text-2xl sm:text-4xl font-bold">{{ nickname }}</span>
          <span class="text-xl sm:text-2xl">{{ username }}</span>
        </div>
      </div>
    </div>

    <div class="container mx-auto">
      <!-- Tab Navigation -->
      <div class="flex justify-start mb-8 space-x-5 overflow-x-auto sm:overflow-visible">
        <div
          @click="setView('account')"
          :class="getTabClass('account')"
          class="tab text-sm sm:text-base"
        >
          Account
        </div>
        <div
          @click="setView('myGroups')"
          :class="getTabClass('myGroups')"
          class="tab text-sm sm:text-base"
        >
          My Groups
        </div>
        <div
          @click="setView('joinGroups')"
          :class="getTabClass('joinGroups')"
          class="tab text-sm sm:text-base"
        >
          Join a Group
        </div>
        <div
          @click="setView('createGroup')"
          :class="getTabClass('createGroup')"
          class="tab text-sm sm:text-base"
        >
          Create a Group
        </div>
      </div>

      <!-- Account Section -->
      <div v-if="currentView === 'account'" class="flex flex-col space-y-4">
        <h2 class="text-2xl font-bold mb-5">Account Information</h2>

        <div v-if="editing">
          <div>
            <label for="nickname" class="block text-lg">Nickname</label>
            <input
              v-model="form.nickname"
              id="nickname"
              type="text"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label for="username" class="block text-lg">Username</label>
            <input
              v-model="form.username"
              id="username"
              type="text"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label for="email" class="block text-lg">Email</label>
            <input
              v-model="form.email"
              id="email"
              type="email"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label for="oldPassword" class="block text-lg">Old Password</label>
            <input
              v-model="form.oldPassword"
              id="oldPassword"
              type="password"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label for="newPassword" class="block text-lg">New Password</label>
            <input
              v-model="form.newPassword"
              id="newPassword"
              type="password"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div>
            <label for="confirmPassword" class="block text-lg">Confirm New Password</label>
            <input
              v-model="form.confirmPassword"
              id="confirmPassword"
              type="password"
              class="border border-gray-300 rounded-lg p-2 w-full"
            />
          </div>

          <div class="flex flex-row items-left gap-4 mt-5">
            <button 
              @click="deleteAccount"
              class="text-red-700 w-full sm:w-40 bg-white border-solid border-2 border-red-700 hover:bg-red-700 hover:text-white px-4 py-2 rounded-lg mt-2"
            >
              Delete Account
            </button>
            <p class="text-red-700 text-center mt-5">Warning: This action cannot be undone.</p>
          </div>

          <div class="flex flex-wrap gap-4 mt-5">
            <button
              @click="updateAccount"
              class="text-white w-full sm:w-40 bg-green-600 hover:bg-green-700 px-4 py-2 rounded mt-2"
            >
              Save Changes
            </button>
            <button
              @click="cancelEdit"
              class="text-white w-full sm:w-40 bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded mt-2"
            >
              Cancel
            </button>
          </div>
        </div>

        <div v-else>
          <div class="block text-xl text-gray-700"><strong>Nickname:</strong> {{ nickname }}</div>
          <div class="block text-xl text-gray-700"><strong>Username:</strong> {{ username }}</div>
          <div class="block text-xl text-gray-700"><strong>Email:</strong> {{ email }}</div>

          <div class="flex flex-wrap gap-4 mt-5">
            <button
              @click="logout"
              class="text-white w-full sm:w-40 bg-red-600 hover:bg-red-700 px-4 py-2 rounded mt-2"
            >
              Logout
            </button>
            <button
              @click="startEdit"
              class="text-white w-full sm:w-40 bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded mt-2"
            >
              Edit Account
            </button>
          </div>
        </div>
      </div>

      <!-- My Groups Section -->
      <div v-if="currentView === 'myGroups'">
        <h2 class="text-2xl font-semibold mb-4">My Groups</h2>
        <ul v-if="groups.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <li v-for="group in groups" :key="group.id" class="bg-white rounded-lg border-solid border-2  p-4">
            <div class="block text-xl text-gray-700"><strong>{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></strong> {{ group.description }}</div>
            <div class="block text-xl text-gray-700">{{ group.members.length }} members.</div>
            <div class="block text-xl text-gray-700"> {{ group.description }}</div>
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
        <ul v-if="availableGroups.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
          <li v-for="group in availableGroups" :key="group.id" class="bg-white rounded-lg shadow p-4">
            <div class="block text-xl text-gray-700"><strong>{{ group.name }} <span v-if="!group.is_public" class="text-red-500">(Private)</span></strong> {{ group.description }}</div>
            <div class="block text-xl text-gray-700">{{ group.members.length }} members.</div>
            <div class="block text-xl text-gray-700"> {{ group.description }}</div>
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

      <!-- Success and Error Messages -->
      <div v-if="successMessage" class="text-green-500 text-center mt-4">{{ successMessage }}</div>
      <div v-if="errorMessage" class="text-red-500 text-center mt-4">{{ errorMessage }}</div>
    </div>
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
    this.fetchUserGroups();
    this.fetchPublicGroups();
  },
  methods: {
    setView(view) {
      this.currentView = view;
      if (view === 'joinGroups') this.fetchAvailableGroups();
    },
    getTabClass(view) {
    return this.currentView === view
      ? 'tab active'
      : 'tab text-gray-600'; // Default state for non-active tabs
    },
    startEdit() {
      this.editing = true; // Start editing mode
    },
    cancelEdit() {
      this.editing = false; // Cancel editing
    },
    async updateAccount() {
      try {
        const updatedFields = {};

        // Log the request data to inspect it
        console.log('Form data being sent:', this.form);

        // Check if the old password is provided
        if (this.form.oldPassword) {
          const passwordMatchResponse = await axios.post('/check-password', {
            password: this.form.oldPassword  // This should be sent as 'password'
          });

          // Check the response to see if the old password is correct
          console.log('Password check response:', passwordMatchResponse);

          // If the password is incorrect, show an error
          if (passwordMatchResponse.status !== 200) {
            this.errorMessage = 'Old password is incorrect.';
            this.successMessage = '';
            return;
          }
        }

        // Proceed with other checks for password and form fields
        if (this.form.newPassword !== this.form.confirmPassword) {
          this.errorMessage = 'New password and confirm password do not match.';
          this.successMessage = '';
          return;
        }

        // Other form update fields (username, email, etc.)
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

        console.log('Fields being updated:', updatedFields);

        // Send the update request
        const response = await axios.put('/update-user', updatedFields);
        console.log('Account update response:', response);
        
        this.successMessage = response.data.message;
        this.errorMessage = '';
        this.editing = false;  // Exit edit mode
      } catch (error) {
        console.error('Error updating account:', error);  // Log the error to inspect it
        this.errorMessage = error.response?.data?.message || 'An error occurred while updating the account';
        this.successMessage = '';
      }
    },
    async deleteAccount() {
      if (confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
        try {
          const response = await this.$axios.delete('http://localhost:5000/delete_account');
          if (response.data.success) {
            alert(response.data.message); 
            window.location.href = "/";  
          } else {
            alert(response.data.message); 
          }
        } catch (error) {
          console.error("Error deleting account:", error);
          alert("Failed to delete account. Please try again.");
        }
      }
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
      console.log("Group to leave", groupId);
      console.log("User that leaves", this.username);
      try {
        await axios.post(`/groups/${groupId}/leave`);
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

