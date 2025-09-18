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
        <div
          @click="setView('invitations')"
          :class="[
            'cursor-pointer py-3 px-4 transition-all duration-300 flex items-center',
            currentView === 'invitations'
              ? 'bg-[#B03052] text-white font-bold'
              : 'text-gray-600 hover:bg-[#D76C82]/10 hover:text-[#B03052] font-semibold'
          ]"
        >
          Invitations
          <span v-if="pendingInvitations.length > 0" class="ml-2 px-2 py-1 bg-red-500 text-white text-xs rounded-full">{{ pendingInvitations.length }}</span>
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
              <div class="flex gap-2 mt-4 items-stretch">

                <button
                  v-if="group.owner.id === currentUser.id && !group.is_public"
                  @click="openInviteModal(group)"
                  class="flex-1 px-4 h-12 bg-[#B03052] text-white rounded-xl hover:bg-[#8B2440] transition-all duration-200 font-medium flex items-center justify-center"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Invite
                </button>
                                <button
                  @click="viewMembers(group)"
                  class="flex-1 px-4 h-12 bg-white text-[#B03052] rounded-xl border-2 border-[#B03052] hover:bg-[#B03052] hover:text-white transition-all duration-200 font-medium flex items-center justify-center"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Members
                </button>

                <!-- Dropdown Menu -->
                <div class="relative">
                  <button
                    @click.stop="toggleGroupMenu(group.id)"
                    class="px-3 w-12 h-12 bg-white text-gray-600 rounded-xl hover:bg-gray-100 transition-all duration-200 border-2 border-gray-300 flex items-center justify-center"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none">
                      <path d="M12 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM12 6a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM12 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" fill="currentColor" stroke="currentColor" stroke-width="2"/>
                    </svg>
                  </button>

                  <!-- Dropdown Content -->
                  <div v-if="openGroupMenu === group.id"
                       @click.stop
                       class="absolute right-0 top-14 w-48 bg-white rounded-lg shadow-xl border border-gray-200 z-50">
                    <button
                      v-if="group.owner.id === currentUser.id"
                      @click="openEditGroupModal(group); openGroupMenu = null"
                      class="w-full text-left px-4 py-3 text-gray-700 hover:bg-gray-50 flex items-center gap-2 rounded-t-lg transition-colors"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                        <path d="M11 4H4C3.44772 4 3 4.44772 3 5V20C3 20.5523 3.44772 21 4 21H19C19.5523 21 20 20.5523 20 20V13M18.5 2.5C19.3284 1.67157 20.6716 1.67157 21.5 2.5C22.3284 3.32843 22.3284 4.67157 21.5 5.5L12 15L8 16L9 12L18.5 2.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      Edit Group
                    </button>
                    <button
                      @click="leaveGroup(group.id); openGroupMenu = null"
                      :class="group.owner.id === currentUser.id ? 'border-t border-gray-200' : 'rounded-t-lg'"
                      class="w-full text-left px-4 py-3 text-gray-700 hover:bg-gray-50 flex items-center gap-2 transition-colors"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                        <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      Leave Group
                    </button>
                    <button
                      v-if="group.owner.id === currentUser.id"
                      @click="deleteGroup(group.id); openGroupMenu = null"
                      class="w-full text-left px-4 py-3 text-red-600 hover:bg-red-50 flex items-center gap-2 rounded-b-lg border-t border-gray-200 transition-colors"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                        <path d="M14 10V17M10 10V17M6 7V18C6 19.1046 6.89543 20 8 20H16C17.1046 20 18 19.1046 18 18V7M6 7H8M6 7H4M8 7V5C8 3.89543 8.89543 3 10 3H14C15.1046 3 16 3.89543 16 5V7M8 7H16M16 7H18M16 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      Delete Group
                    </button>
                  </div>
                </div>
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

        <!-- Invitations Section -->
        <div v-if="currentView === 'invitations'">
          <h2 class="text-3xl font-bold mb-6 text-gray-800">My Invitations</h2>

          <div v-if="loadingInvitations" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="pendingInvitations.length" class="space-y-4">
            <div v-for="invitation in pendingInvitations" :key="invitation.id"
                 class="bg-white rounded-lg shadow-md p-6 border border-[#D76C82]/10">
              <div class="flex justify-between items-center">
                <div>
                  <h3 class="text-xl font-bold text-gray-800 mb-2">{{ invitation.group.name }}</h3>
                  <p class="text-gray-600 mb-2">{{ invitation.group.description }}</p>
                  <p class="text-sm text-gray-500">Invited by: {{ invitation.sender.username }}</p>
                </div>
                <div class="flex gap-3">
                  <button
                    @click="acceptInvitation(invitation.id)"
                    class="px-6 py-3 bg-[#B03052] text-white rounded-lg hover:bg-[#8B2440] transition-colors duration-300 font-medium"
                  >
                    Accept
                  </button>
                  <button
                    @click="rejectInvitation(invitation.id)"
                    class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
                  >
                    Decline
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="bg-white rounded-lg shadow-md p-8 text-center border border-[#D76C82]/10">
            <p class="text-gray-600">You don't have any pending invitations.</p>
          </div>
        </div>
        </div>
      </div>
    </section>

    <!-- Invite Modal -->
    <div v-if="showInviteModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl p-8 max-w-md w-full mx-4">
        <h3 class="text-2xl font-bold mb-4 text-gray-800">Invite Members to {{ selectedGroup?.name }}</h3>

        <!-- User Search -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-2">Search Users</label>
          <input
            v-model="userSearchQuery"
            @input="searchUsers"
            type="text"
            placeholder="Type username or nickname..."
            class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent"
          />
        </div>

        <!-- Search Results -->
        <div v-if="searchResults.length" class="max-h-60 overflow-y-auto mb-4 border border-gray-200 rounded-lg">
          <div v-for="user in searchResults" :key="user.id"
               class="p-3 hover:bg-gray-50 cursor-pointer flex justify-between items-center"
               @click="selectUserToInvite(user)">
            <div>
              <p class="font-medium">{{ user.username }}</p>
              <p class="text-sm text-gray-600">{{ user.nickname }}</p>
            </div>
            <button
              v-if="!isUserInvited(user.id)"
              class="px-3 py-1 bg-[#B03052] text-white rounded-lg hover:bg-[#8B2440] text-sm"
            >
              Invite
            </button>
            <span v-else class="text-sm text-gray-500">Already invited</span>
          </div>
        </div>
        <div v-else-if="userSearchQuery && !searchingUsers" class="text-gray-600 mb-4">
          No users found
        </div>

        <!-- Pending Invitations -->
        <div v-if="groupInvitations.length" class="mb-4">
          <h4 class="font-medium text-gray-700 mb-2">Pending Invitations</h4>
          <div class="space-y-2">
            <div v-for="invitation in groupInvitations" :key="invitation.id"
                 class="flex justify-between items-center p-2 bg-gray-50 rounded">
              <span>{{ invitation.recipient.username }}</span>
              <button
                @click="cancelInvitation(invitation.id)"
                class="text-red-600 hover:text-red-800 text-sm"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>

        <!-- Modal Actions -->
        <div class="flex justify-end gap-3 mt-6">
          <button
            @click="closeInviteModal"
            class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
          >
            Close
          </button>
        </div>
      </div>
    </div>

    <!-- Members Modal -->
    <div v-if="showMembersModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl p-8 max-w-md w-full mx-4">
        <h3 class="text-2xl font-bold mb-4 text-gray-800">{{ selectedGroup?.name }} Members</h3>

        <div class="max-h-96 overflow-y-auto">
          <div v-for="member in selectedGroupMembers" :key="member.id"
               class="py-3 px-4 hover:bg-gray-50 rounded-lg flex justify-between items-center">
            <div>
              <p class="font-medium text-gray-800">{{ member.username }}</p>
              <p class="text-sm text-gray-600">{{ member.nickname || member.username }}</p>
            </div>
            <span v-if="selectedGroup?.owner.id === member.id"
                  class="px-2 py-1 bg-[#B03052] text-white text-xs rounded-full">Owner</span>
          </div>
        </div>

        <div class="flex justify-end gap-3 mt-6">
          <button
            @click="closeMembersModal"
            class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
          >
            Close
          </button>
        </div>
      </div>
    </div>

    <!-- Edit Group Modal -->
    <div v-if="showEditGroupModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl p-8 max-w-md w-full mx-4">
        <h3 class="text-2xl font-bold mb-4 text-gray-800">Edit Group</h3>

        <form @submit.prevent="updateGroup">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Group Name</label>
            <input
              v-model="editGroupForm.name"
              type="text"
              required
              class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent"
            />
          </div>

          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea
              v-model="editGroupForm.description"
              rows="3"
              class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-[#B03052] focus:border-transparent"
            />
          </div>

          <div class="mb-6">
            <label class="flex items-center">
              <input
                v-model="editGroupForm.is_public"
                type="checkbox"
                class="mr-2 rounded border-gray-300 text-[#B03052] focus:ring-[#B03052]"
              />
              <span class="text-sm font-medium text-gray-700">Public Group (visible to all users)</span>
            </label>
          </div>

          <div class="flex justify-end gap-3">
            <button
              type="button"
              @click="closeEditGroupModal"
              class="px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors duration-300 font-medium"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-6 py-3 bg-[#B03052] text-white rounded-lg hover:bg-[#8B2440] transition-colors duration-300 font-medium"
            >
              Save Changes
            </button>
          </div>
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
      // New invitation properties
      showInviteModal: false,
      selectedGroup: null,
      userSearchQuery: '',
      searchResults: [],
      searchingUsers: false,
      groupInvitations: [],
      pendingInvitations: [],
      loadingInvitations: false,
      // Members modal
      showMembersModal: false,
      selectedGroupMembers: [],
      // Dropdown menu
      openGroupMenu: null,
      // Edit group modal
      showEditGroupModal: false,
      editGroupForm: {
        id: null,
        name: '',
        description: '',
        is_public: false,
      },
    };
  },
  mounted() {
    this.toast = useToast();
    this.fetchUserGroups();
    this.fetchPublicGroups();
    this.fetchAvailableGroups(); // Load available groups on mount
    this.fetchInvitations(); // Load user's invitations
    // Initialize form with current values
    this.form.nickname = this.getNickname;
    this.form.username = this.getUsername;
    this.form.email = this.getEmail;

    // Add click outside handler for dropdown
    this.handleClickOutside = (event) => {
      // Check if click is outside of dropdown button and dropdown content
      const dropdownButton = event.target.closest('button[class*="w-12 h-12"]');
      const dropdownContent = event.target.closest('div[class*="absolute right-0 top-14"]');

      if (!dropdownButton && !dropdownContent) {
        this.openGroupMenu = null;
      }
    };
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
    // Clean up event listener
    if (this.handleClickOutside) {
      document.removeEventListener('click', this.handleClickOutside);
    }
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
      } else if (view === 'invitations') {
        this.fetchInvitations();
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
        
        this.toast.success('Account details updated successfully.');
        
        // Update the store with new user info
        await this.$store.dispatch('checkAuth');
      } catch (error) {
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
            this.toast.error('Failed to delete account. Please try again.');
          }
        } catch (error) {
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
        }
      }
    },
    async fetchAvailableGroups() {
      this.loadingAvailableGroups = true;
      try {
        // Get all public groups first
        const response = await axios.get('/groups');
        // Show all public groups, marking which ones the user is already in
        const publicGroups = response.data.filter(group => group.is_public);
        
        // Add a flag to indicate if user is already a member
        this.availableGroups = publicGroups.map(group => ({
          ...group,
          isMember: group.members.some(member => member.username === this.username)
        }));
        
      } catch (error) {
        if (error.response?.status === 401) {
          this.availableGroups = [];
        } else {
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
    // New invitation methods
    async openInviteModal(group) {
      this.selectedGroup = group;
      this.showInviteModal = true;
      this.userSearchQuery = '';
      this.searchResults = [];
      await this.fetchGroupInvitations(group.id);
    },
    closeInviteModal() {
      this.showInviteModal = false;
      this.selectedGroup = null;
      this.userSearchQuery = '';
      this.searchResults = [];
      this.groupInvitations = [];
    },
    async searchUsers() {
      if (!this.userSearchQuery.trim()) {
        this.searchResults = [];
        return;
      }

      this.searchingUsers = true;
      try {
        const response = await axios.get(`/users/search?query=${this.userSearchQuery}`);
        // Filter out users who are already members
        this.searchResults = response.data.filter(
          user => !this.selectedGroup.members.some(member => member.id === user.id)
        );
      } catch (error) {
      } finally {
        this.searchingUsers = false;
      }
    },
    async selectUserToInvite(user) {
      try {
        await axios.post(`/groups/${this.selectedGroup.id}/invite`, {
          recipient_id: user.id
        });
        this.toast.success(`Invitation sent to ${user.username}`);
        await this.fetchGroupInvitations(this.selectedGroup.id);
        // Remove user from search results
        this.searchResults = this.searchResults.filter(u => u.id !== user.id);
      } catch (error) {
        if (error.response?.data?.message) {
          this.toast.error(error.response.data.message);
        } else {
          this.toast.error('Failed to send invitation');
        }
      }
    },
    isUserInvited(userId) {
      return this.groupInvitations.some(inv => inv.recipient.id === userId);
    },
    async fetchGroupInvitations(groupId) {
      try {
        const response = await axios.get(`/groups/${groupId}/invitations`);
        this.groupInvitations = response.data;
      } catch (error) {
      }
    },
    async cancelInvitation(invitationId) {
      try {
        await axios.delete(`/invitations/${invitationId}/cancel`);
        this.toast.success('Invitation cancelled');
        await this.fetchGroupInvitations(this.selectedGroup.id);
      } catch (error) {
        this.toast.error('Failed to cancel invitation');
      }
    },
    async fetchInvitations() {
      this.loadingInvitations = true;
      try {
        const response = await axios.get('/invitations');
        this.pendingInvitations = response.data;
      } catch (error) {
        if (error.response?.status !== 401) {
        }
      } finally {
        this.loadingInvitations = false;
      }
    },
    async acceptInvitation(invitationId) {
      try {
        await axios.post(`/invitations/${invitationId}/accept`);
        this.toast.success('Invitation accepted! You have joined the group.');
        await this.fetchInvitations();
        await this.fetchUserGroups();
      } catch (error) {
        this.toast.error('Failed to accept invitation');
      }
    },
    async rejectInvitation(invitationId) {
      try {
        await axios.post(`/invitations/${invitationId}/reject`);
        this.toast.info('Invitation declined');
        await this.fetchInvitations();
      } catch (error) {
        this.toast.error('Failed to reject invitation');
      }
    },
    // Members modal methods
    viewMembers(group) {
      this.selectedGroup = group;
      this.selectedGroupMembers = group.members;
      this.showMembersModal = true;
    },
    closeMembersModal() {
      this.showMembersModal = false;
      this.selectedGroupMembers = [];
    },
    // Dropdown menu method
    toggleGroupMenu(groupId) {
      this.openGroupMenu = this.openGroupMenu === groupId ? null : groupId;
    },
    // Edit group methods
    openEditGroupModal(group) {
      this.editGroupForm = {
        id: group.id,
        name: group.name,
        description: group.description || '',
        is_public: group.is_public,
      };
      this.showEditGroupModal = true;
    },
    closeEditGroupModal() {
      this.showEditGroupModal = false;
      this.editGroupForm = {
        id: null,
        name: '',
        description: '',
        is_public: false,
      };
    },
    async updateGroup() {
      try {
        const response = await axios.put(`/groups/${this.editGroupForm.id}`, {
          name: this.editGroupForm.name,
          description: this.editGroupForm.description,
          is_public: this.editGroupForm.is_public,
        });
        this.toast.success('Group updated successfully!');
        this.closeEditGroupModal();
        // Refresh the groups list
        await this.fetchUserGroups();
        await this.fetchAvailableGroups();
      } catch (error) {
        if (error.response) {
          this.toast.error(error.response.data?.message || 'Failed to update group. Please try again.');
        } else {
          this.toast.error('Failed to update group. Please try again.');
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