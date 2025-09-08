<template>
  <div v-if="isAuthenticated" class="mx-4">
    <section class="flex">
      <!-- Sidebar for Account Sections -->
      <div class="w-1/6 bg-[#FEFEFD] py-4 h-screen overflow-y-auto border-r border-gray-300/20">
        <h2 class="text-2xl font-bold mb-6 text-gray-800 px-4">Account</h2>
        <div 
          @click="setView('account')"
          :class="[
            'cursor-pointer py-3 px-4 transition-all duration-300 flex items-center',
            currentView === 'account' 
              ? 'bg-[#B03052] text-white font-bold' 
              : 'text-gray-600 hover:bg-[#D76C82]/10 hover:text-[#B03052] font-semibold'
          ]"
        >
          Profile
        </div>
        <div 
          @click="setView('myGroups')"
          :class="[
            'cursor-pointer py-3 px-4 transition-all duration-300 flex items-center',
            currentView === 'myGroups' 
              ? 'bg-[#B03052] text-white font-bold' 
              : 'text-gray-600 hover:bg-[#D76C82]/10 hover:text-[#B03052] font-semibold'
          ]"
        >
          My Groups
        </div>
        <div 
          @click="setView('joinGroups')"
          :class="[
            'cursor-pointer py-3 px-4 transition-all duration-300 flex items-center',
            currentView === 'joinGroups' 
              ? 'bg-[#B03052] text-white font-bold' 
              : 'text-gray-600 hover:bg-[#D76C82]/10 hover:text-[#B03052] font-semibold'
          ]"
        >
          Join Groups
        </div>
      </div>
      <div class="min-h-[1em] w-px self-stretch bg-gradient-to-tr from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400"></div>
      
      <!-- Main section for content -->
      <div class="flex-1 bg-[#FEFEFD] py-8 px-12 flex justify-center">
        <div class="w-full max-w-5xl">
        <!-- Account Section -->
        <div v-if="currentView === 'account'">
          <h2 class="text-3xl font-bold mb-10 text-gray-800">Profile Information</h2>
          
          <!-- Profile Info Card -->
          <div class="bg-white rounded-lg shadow-md mb-4 border border-[#D76C82]/10">
            <div class="px-8 py-10">
              <h3 class="text-xl font-semibold text-gray-800 mb-8">Account Details</h3>
              
              <div class="space-y-4 px-4">
              <div>
                <label for="nickname" class="block text-sm font-medium text-gray-700 mb-2">Nickname</label>
                <input
                  v-model="form.nickname"
                  id="nickname"
                  type="text"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Enter your nickname"
                />
              </div>

              <div>
                <label for="username" class="block text-sm font-medium text-gray-700 mb-2">Username</label>
                <input
                  v-model="form.username"
                  id="username"
                  type="text"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Enter your username"
                />
              </div>

              <div>
                <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
                <input
                  v-model="form.email"
                  id="email"
                  type="email"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Enter your email"
                />
              </div>

              <div class="flex items-center gap-4 pt-6">
                <button
                  @click="updateAccount"
                  class="bg-[#B03052] text-white px-8 py-3 rounded-lg hover:bg-[#8B2440] transition-colors duration-300 font-medium"
                >
                  Save Changes
                </button>
                <button
                  @click="resetForm"
                  class="bg-gray-200 text-gray-700 px-8 py-3 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
                >
                  Reset
                </button>
              </div>
              </div>
            </div>
          </div>

          <!-- Password Change Card -->
          <div class="bg-white rounded-lg shadow-md mb-4 border border-[#D76C82]/10">
            <div class="px-8 py-10">
              <h3 class="text-xl font-semibold text-gray-800 mb-8">Password & Security</h3>
              
              <div v-if="showPasswordSection" class="space-y-4 px-4">
              <div>
                <label for="oldPassword" class="block text-sm font-medium text-gray-700 mb-2">Current Password</label>
                <input
                  v-model="form.oldPassword"
                  id="oldPassword"
                  type="password"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Enter your current password"
                />
              </div>

              <div>
                <label for="newPassword" class="block text-sm font-medium text-gray-700 mb-2">New Password</label>
                <input
                  v-model="form.newPassword"
                  id="newPassword"
                  type="password"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Enter your new password"
                />
              </div>

              <div>
                <label for="confirmPassword" class="block text-sm font-medium text-gray-700 mb-2">Confirm New Password</label>
                <input
                  v-model="form.confirmPassword"
                  id="confirmPassword"
                  type="password"
                  class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent text-base"
                  placeholder="Confirm your new password"
                />
              </div>

              <div class="flex gap-4 pt-6">
                <button
                  @click="updatePassword"
                  class="bg-[#B03052] text-white px-8 py-3 rounded-lg hover:bg-[#8B2440] transition-colors duration-300 font-medium"
                >
                  Update Password
                </button>
                <button
                  @click="showPasswordSection = false; form.oldPassword = ''; form.newPassword = ''; form.confirmPassword = ''"
                  class="bg-gray-200 text-gray-700 px-8 py-3 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
                >
                  Cancel
                </button>
              </div>
            </div>
              
              <div v-else>
                <div class="text-gray-600 mb-6 px-4">
                  <p>Keep your account secure by using a strong password.</p>
                </div>
                <div class="flex justify-start px-4">
                  <button
                    @click="showPasswordSection = true"
                    class="bg-[#B03052] text-white px-6 py-3 rounded-lg hover:bg-[#8B2440] transition-colors duration-300 font-medium flex items-center gap-2"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"/>
                    </svg>
                    Change Password
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Account Actions Card -->
          <div class="bg-white rounded-lg shadow-md border border-[#D76C82]/10">
            <div class="px-8 py-10">
              <h3 class="text-xl font-semibold text-gray-800 mb-8">Account Actions</h3>
              
              <div class="space-y-6 px-4">
                <!-- Logout Section -->
                <div class="pb-6 border-b border-gray-200">
                  <div class="flex items-center justify-between">
                    <div>
                      <h4 class="font-medium text-gray-900 mb-1">Sign Out</h4>
                      <p class="text-sm text-gray-600">End your current session and return to login</p>
                    </div>
                    <button
                      @click="logout"
                      class="bg-gray-600 text-white px-8 py-3 rounded-lg hover:bg-gray-700 transition-colors duration-300 font-medium flex items-center gap-2"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
                      </svg>
                      Logout
                    </button>
                  </div>
                </div>
                
                <!-- Delete Account Section -->
                <div>
                  <div class="flex items-center justify-between">
                    <div>
                      <h4 class="font-medium text-red-600 mb-1">Danger Zone</h4>
                      <p class="text-sm text-gray-600">Permanently delete your account and all associated data</p>
                    </div>
                    <button 
                      @click="deleteAccount"
                      class="text-red-600 border-2 border-red-600 px-8 py-3 rounded-lg hover:bg-red-600 hover:text-white transition-colors duration-300 font-medium flex items-center gap-2"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                      </svg>
                      Delete Account
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- My Groups Section -->
        <div v-if="currentView === 'myGroups'">
          <h2 class="text-3xl font-bold mb-6 text-gray-800">My Groups</h2>
          
          <div v-if="loadingGroups" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="groups.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
            <div v-for="group in groups" :key="group.id" 
                 class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-6 flex flex-col min-h-[280px] border border-[#D76C82]/10">
              <div class="flex-grow flex flex-col overflow-hidden">
                <h3 class="text-xl font-bold text-gray-800 my-3 break-words">
                  {{ group.name }} 
                  <span v-if="!group.is_public" class="text-[#B03052] text-sm font-semibold">(Private)</span>
                </h3>
                <p class="text-gray-600 mb-3 break-words">{{ group.description }}</p>
                <div class="mt-auto">
                  <div class="text-sm text-gray-600 mb-2">
                    <span class="font-medium">Owner:</span> {{ group.owner.username }}
                  </div>
                  <div class="text-sm text-gray-600">
                    <span class="font-medium">Members:</span> {{ group.members.length }}
                  </div>
                </div>
              </div>
              
              <!-- Action Buttons -->
              <div class="flex gap-2 mt-4">
                <button
                  @click="leaveGroup(group.id)"
                  class="flex-1 px-4 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600 font-medium"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 inline mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Leave
                </button>
                <button
                  v-if="group.owner.id === currentUser.id"
                  @click="deleteGroup(group.id)"
                  class="px-3 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M14 10V17M10 10V17M6 7V18C6 19.1046 6.89543 20 8 20H16C17.1046 20 18 19.1046 18 18V7M6 7H8M6 7H4M8 7V5C8 3.89543 8.89543 3 10 3H14C15.1046 3 16 3.89543 16 5V7M8 7H16M16 7H18M16 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="bg-white rounded-lg shadow-md p-8 text-center border border-[#D76C82]/10">
            <p class="text-gray-600">You haven't joined any groups yet.</p>
          </div>
        </div>

        <!-- Join Groups Section -->
        <div v-if="currentView === 'joinGroups'">
          <h2 class="text-3xl font-bold mb-6 text-gray-800">Discover Groups</h2>
          
          <div class="bg-white rounded-lg shadow-md p-6 mb-6 border border-[#D76C82]/10">
            <div class="flex gap-3">
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search for groups..."
                @keyup.enter="searchGroups"
                class="flex-1 border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent"
              />
              <button 
                @click="searchGroups" 
                class="bg-[#B03052] text-white px-6 py-3 rounded-lg hover:bg-[#8B2440] transition-colors duration-300"
              >
                Search
              </button>
            </div>
          </div>

          <div v-if="loadingAvailableGroups" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="availableGroups.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
            <div v-for="group in availableGroups" :key="group.id" 
                 class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-6 flex flex-col min-h-[280px] border border-[#D76C82]/10">
              <div class="flex-grow flex flex-col overflow-hidden">
                <h3 class="text-xl font-bold text-gray-800 my-3 break-words">
                  {{ group.name }}
                  <span v-if="!group.is_public" class="text-[#B03052] text-sm font-semibold">(Private)</span>
                </h3>
                <p v-if="group.description" class="text-gray-600 mb-3 break-words">{{ group.description }}</p>
                <div class="mt-auto">
                  <div class="text-sm text-gray-600 mb-2">
                    <span class="font-medium">Owner:</span> {{ group.owner.username }}
                  </div>
                  <div class="text-sm text-gray-600">
                    <span class="font-medium">Members:</span> {{ group.members.length }}
                  </div>
                </div>
              </div>
              
              <!-- Action Buttons -->
              <div class="flex gap-2 mt-4">
                <button
                  v-if="group.isMember"
                  @click="leaveGroup(group.id)"
                  class="flex-1 px-4 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600 font-medium"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 inline mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Leave
                </button>
                <button
                  v-else
                  @click="joinGroup(group.id)"
                  class="flex-1 flex items-center justify-center px-4 py-2.5 rounded-xl font-medium transition-all duration-200 bg-[#B03052] text-white hover:bg-[#8B2440]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M14 3V5M14 5V7M14 5H16M14 5H12M19 10V21H5V10M10 21V15H14V21M3 10L12 3L21 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Join Group
                </button>
              </div>
            </div>
          </div>
          <div v-else class="bg-white rounded-lg shadow-md p-8 text-center border border-[#D76C82]/10">
            <p class="text-gray-600">No public groups found. Try searching or creating a new group.</p>
          </div>
        </div>
        </div>
      </div>
    </section>
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
      showPasswordSection: false,
      loadingGroups: false,
      loadingAvailableGroups: false,
      openGroupId: null,
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
    this.fetchAvailableGroups(); // Load available groups on mount
    // Initialize form with current values
    this.form.nickname = this.getNickname;
    this.form.username = this.getUsername;
    this.form.email = this.getEmail;
  },
  watch: {
    // Watch for changes in user data and update form
    getNickname(newVal) {
      if (!this.showPasswordSection) {
        this.form.nickname = newVal;
      }
    },
    getUsername(newVal) {
      if (!this.showPasswordSection) {
        this.form.username = newVal;
      }
    },
    getEmail(newVal) {
      if (!this.showPasswordSection) {
        this.form.email = newVal;
      }
    }
  },
  methods: {
    async logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
      this.toast.success('You have logged out successfully.');
    },
    
    setView(view) {
      this.currentView = view;
      if (view === 'joinGroups') {
        this.fetchAvailableGroups();
      }
    },
    toggleGroupDropdown(groupId) {
      this.openGroupId = this.openGroupId === groupId ? null : groupId;
    },
    startEdit() {
      this.editing = true; 
    },
    cancelEdit() {
      this.editing = false; 
      this.form = {
        nickname: this.getNickname,
        username: this.getUsername,
        email: this.getEmail,
        oldPassword: '',
        newPassword: '',
        confirmPassword: '',
      };
    },
    resetForm() {
      this.form = {
        nickname: this.getNickname,
        username: this.getUsername,
        email: this.getEmail,
        oldPassword: '',
        newPassword: '',
        confirmPassword: '',
      };
      this.showPasswordSection = false;
    },
    async updateAccount() {
      try {
        const updatedFields = {};

        if (this.form.nickname !== this.getNickname) {
          updatedFields.nickname = this.form.nickname;
        }
        if (this.form.username !== this.getUsername) {
          updatedFields.username = this.form.username;
        }
        if (this.form.email !== this.getEmail) {
          updatedFields.email = this.form.email;
        }

        if (Object.keys(updatedFields).length === 0) {
          this.toast.info('No changes to save.');
          return;
        }

        const response = await axios.put('/update-user', updatedFields);
        
        console.log('Account updated:', response.data);
        this.toast.success('Account details updated successfully.');
        
        // Update the store with new user info
        await this.$store.dispatch('checkAuth');
      } catch (error) {
        console.error('Error updating account:', error); 
        this.toast.error('An error occurred while updating the account');
      }
    },
    async updatePassword() {
      try {
        if (!this.form.oldPassword) {
          this.toast.error('Please enter your current password.');
          return;
        }

        if (!this.form.newPassword) {
          this.toast.error('Please enter a new password.');
          return;
        }

        if (this.form.newPassword !== this.form.confirmPassword) {
          this.toast.error('New passwords do not match.');
          return;
        }

        // Verify old password
        const passwordMatchResponse = await axios.post('/check-password', {
          password: this.form.oldPassword
        });

        if (passwordMatchResponse.status !== 200) {
          this.toast.error('Current password is incorrect.');
          return;
        }

        // Update password
        await axios.put('/update-user', {
          password: this.form.newPassword
        });
        
        this.toast.success('Password updated successfully.');
        
        // Clear password fields
        this.form.oldPassword = '';
        this.form.newPassword = '';
        this.form.confirmPassword = '';
        this.showPasswordSection = false;
      } catch (error) {
        console.error('Error updating password:', error); 
        this.toast.error('An error occurred while updating the password');
      }
    },
    async deleteAccount() {
      if (confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
        try {
          const response = await axios.delete('/delete_account');
          if (response.data.success) {
            this.toast.success(response.data.message);
            this.$store.dispatch('logout');
            this.$router.push('/');
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
      this.loadingGroups = true;
      try {
        const response = await axios.get('/groups/mine');
        this.groups = response.data;
      } catch (error) {
        if (error.response?.status === 401) {
          this.groups = [];
        } else {
          console.log('Error fetching user groups:', error);
        }
      } finally {
        this.loadingGroups = false;
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
      this.loadingAvailableGroups = true;
      try {
        // Get all public groups first
        const response = await axios.get('/groups');
        console.log('All groups from API:', response.data);
        console.log('Current user:', this.currentUser);
        console.log('Username:', this.username);
        
        // Show all public groups, marking which ones the user is already in
        const publicGroups = response.data.filter(group => group.is_public);
        
        // Add a flag to indicate if user is already a member
        this.availableGroups = publicGroups.map(group => ({
          ...group,
          isMember: group.members.some(member => member.username === this.username)
        }));
        
        console.log('Available groups with membership status:', this.availableGroups);
      } catch (error) {
        if (error.response?.status === 401) {
          this.availableGroups = [];
        } else {
          console.error('Error fetching available groups:', error);
        }
      } finally {
        this.loadingAvailableGroups = false;
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
        this.setView('myGroups');
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
          // Remove group from My Groups list
          this.groups = this.groups.filter(group => group.id !== groupId);
        }
        // Refresh both group lists
        this.fetchUserGroups();
        this.fetchAvailableGroups();
      } catch (error) {
        this.toast.error('Error leaving group. Please try again.');
      }
    },
    async searchGroups() {
      try {
        if (this.searchQuery.trim()) {
          // If there's a search query, use the search endpoint
          const response = await axios.get(`/groups/search?query=${this.searchQuery}`);
          // Show all public groups from search results with membership status
          const publicGroups = response.data.filter(group => group.is_public);
          
          // Add a flag to indicate if user is already a member
          this.availableGroups = publicGroups.map(group => ({
            ...group,
            isMember: group.members.some(member => member.username === this.username)
          }));
        } else {
          // If no search query, show all public groups
          this.fetchAvailableGroups();
        }
      } catch (error) {
        console.error('Error searching groups:', error);
        this.toast.error('Error searching groups. Please try again.');
      }
    },
    async deleteGroup(groupId) {
      if (confirm("Are you sure you want to delete this group?")) {
        try {
          await axios.delete(`/groups/${groupId}`);
          this.toast.success('Group deleted successfully!');
          this.fetchUserGroups();
          this.fetchAvailableGroups();
        } catch (error) {
          this.toast.error('Error deleting group. Please try again.');
        }
      }
    },
  },
};
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>