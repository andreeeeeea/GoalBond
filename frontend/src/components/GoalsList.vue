<template>
  <div v-if="isAuthenticated" class="mx-4">   
    <section class="flex">
      <!-- Sidebar for Goal Categories -->
      <div class="w-1/6 bg-[#FEFEFD] py-4 h-screen overflow-y-auto border-r border-gray-300/20">
        <h2 class="text-2xl font-bold mb-6 text-gray-800 px-4">Categories</h2>
          <div 
            v-for="category in goalCategories" 
            :key="category" 
            @click="selectCategory(category)" 
            :class="[
              'cursor-pointer py-3 px-4 transition-all duration-300 flex items-center',
              category === selectedCategory 
                ? 'bg-[#B03052] text-white font-bold' 
                : 'text-gray-600 hover:bg-[#D76C82]/10 hover:text-[#B03052] font-semibold'
            ]"
          >
            {{ category }}
          </div>
      </div>
      <div class=" min-h-[1em] w-px self-stretch bg-gradient-to-tr from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400"></div>
      <!-- Main section for displaying goals -->
      <div class="flex-1 bg-[#FEFEFD] py-6 px-8">
        <h2 class="text-3xl font-bold mb-6 text-gray-800">{{ selectedCategory }}</h2>
        
        <!-- Navigation for Goal Types -->
        <div class="flex space-x-8 mb-8 border-b border-[#D76C82]/20">
          <span 
            @click="showPersonalGoals = true; showGroupGoals = false; showCompletedGoals = false"
            :class="[
              'cursor-pointer pb-3 px-2 transition-all duration-300',
              showPersonalGoals 
                ? 'border-b-2 border-[#B03052] text-[#B03052] font-semibold' 
                : 'text-gray-600 hover:text-[#D76C82]'
            ]"
          >
            Personal Goals
          </span>
          <span 
            @click="showPersonalGoals = false; showGroupGoals = true; showCompletedGoals = false"
            :class="[
              'cursor-pointer pb-3 px-2 transition-all duration-300',
              showGroupGoals 
                ? 'border-b-2 border-[#B03052] text-[#B03052] font-semibold' 
                : 'text-gray-600 hover:text-[#D76C82]'
            ]"
          >
            Group Goals
          </span>
          <span 
            @click="showPersonalGoals = false; showGroupGoals = false; showCompletedGoals = true"
            :class="[
              'cursor-pointer pb-3 px-2 transition-all duration-300',
              showCompletedGoals 
                ? 'border-b-2 border-[#B03052] text-[#B03052] font-semibold' 
                : 'text-gray-600 hover:text-[#D76C82]'
            ]"
          >
            Completed Goals
          </span>
        </div>

        <!-- Display Goals Based on the Selected Type -->
        <div v-if="showPersonalGoals" class="py-4">
          <div v-if="loadingGoals" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="personalGoalsByCategory.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
            <div v-for="goal in personalGoalsByCategory" :key="goal.id" 
                 class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-6 flex flex-col min-h-[280px] border border-[#D76C82]/10">
              <div class="flex-grow flex flex-col overflow-hidden">
                <h3 class="text-xl font-bold text-gray-800 my-3 break-words">{{ goal.title }}</h3>
                <p class="text-gray-600 mb-3 break-words">{{ goal.description }}</p>
                <div v-if="goal.season && goal.episode" class="text-gray-600 mb-2">
                  Season: {{ goal.season }} Episode: {{ goal.episode }}
                </div>
                
                <!-- Progress Section -->
                <div class="my-4">
                  <div class="flex justify-between items-center mb-2">
                    <span class="text-gray-600 text-sm font-medium">Progress</span>
                    <span class="text-[#B03052] text-sm font-bold">{{ goal.progress || 0 }}%</span>
                  </div>
                  <div class="relative w-full bg-gray-200 rounded-full h-2 overflow-hidden">
                    <div
                      class="absolute top-0 left-0 h-full bg-gradient-to-r from-[#B03052] to-[#D76C82] rounded-full transition-all duration-700 ease-out"
                      :style="{ width: `${goal.progress || 0}%` }"
                    />
                  </div>
                </div>
                <div class="flex flex-row mt-auto space-x-2">
                  <div v-if="goal.deadline" class="mt-auto">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M12 7V12L14.5 10.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>

                  <div v-if="goal.deadline" class="mt-auto">
                    <span v-if="(new Date(goal.deadline) - new Date()) > 86400000" class="text-gray-500">
                      {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60 * 24)) }} days left
                    </span>
                    <span v-else-if="(new Date(goal.deadline) - new Date()) > 0" class="text-red-700 font-semibold">
                      {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60)) }} hours left
                    </span>
                    <span v-else class="text-gray-500">
                      Overdue
                    </span>
                  </div>

                  <div class="flex flex-grow justify-end items-center mt-auto space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M3 10H21M7 3V5M17 3V5M6.2 21H17.8C18.9201 21 19.4802 21 19.908 20.782C20.2843 20.5903 20.5903 20.2843 20.782 19.908C21 19.4802 21 18.9201 21 17.8V8.2C21 7.07989 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V17.8C3 18.9201 3 19.4802 3.21799 19.908C3.40973 20.2843 3.71569 20.5903 4.09202 20.782C4.51984 21 5.07989 21 6.2 21Z" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span v-if="goal.deadline" class="text-gray-500">
                      {{ new Date(goal.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) }}
                    </span>
                    <span v-else class="text-gray-500 italic">No deadline</span>
                  </div>
                </div>
                
              </div>

              <!-- Action Buttons -->
              <div class="flex gap-2 mt-4">
                <button
                  @click="toggleGoalCompletion(goal)"
                  :class="[
                    'flex-1 flex items-center justify-center px-4 py-2.5 rounded-xl font-medium transition-all duration-200',
                    goal.completed
                      ? 'bg-green-500 text-white hover:bg-green-600 shadow-lg shadow-green-500/25'
                      : 'bg-[#B03052] text-white hover:bg-[#8B2440] hover:text-white'
                  ]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M9 11L12 14L22 4M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C13.1257 3 14.1978 3.2284 15.1808 3.6358" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  {{ goal.completed ? 'Completed' : 'Complete' }}
                </button>
                
                <button
                  @click="openEditForm(goal)"
                  class="px-3 py-2.5 bg-white text-[#B03052] rounded-xl hover:bg-[#B03052] hover:text-white transition-all duration-200 border-2 border-[#B03052]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M11 4H4C3.44772 4 3 4.44772 3 5V20C3 20.5523 3.44772 21 4 21H19C19.5523 21 20 20.5523 20 20V13M18.5 2.5C19.3284 1.67157 20.6716 1.67157 21.5 2.5C22.3284 3.32843 22.3284 4.67157 21.5 5.5L12 15L8 16L9 12L18.5 2.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                
                <button
                  @click="deleteGoal(goal.id)"
                  class="px-3 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M14 10V17M10 10V17M6 7V18C6 19.1046 6.89543 20 8 20H16C17.1046 20 18 19.1046 18 18V7M6 7H8M6 7H4M8 7V5C8 3.89543 8.89543 3 10 3H14C15.1046 3 16 3.89543 16 5V7M8 7H16M16 7H18M16 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-8 text-gray-600">
            <p>No personal goals found in this category.</p>
          </div>
        </div>

        <!-- Display Group Goals -->
        <div v-if="showGroupGoals" class="py-4">
          <div v-if="loadingGoals" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="groupGoalsByCategory.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
            <div v-for="goal in groupGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-6 flex flex-col min-h-[280px] border border-[#D76C82]/10">
              <div class="flex-grow flex flex-col overflow-hidden">
                <h3 class="text-xl font-bold text-gray-800 my-3 break-words">{{ goal.title }}</h3>
                <p class="text-gray-600 mb-3 break-words">{{ goal.description }}</p>
                <div v-if="goal.season && goal.episode" class="text-gray-600 mb-2">
                  Season: {{ goal.season }} Episode: {{ goal.episode }}
                </div>
                <div class="text-sm text-[#B03052] font-semibold mb-2">Group: {{ goal.group.name }}</div>
                
                <!-- Progress Section -->
                <div class="my-4">
                  <div class="flex justify-between items-center mb-2">
                    <span class="text-gray-600 text-sm font-medium">Progress</span>
                    <span class="text-[#B03052] text-sm font-bold">{{ goal.progress || 0 }}%</span>
                  </div>
                  <div class="relative w-full bg-gray-200 rounded-full h-2 overflow-hidden">
                    <div
                      class="absolute top-0 left-0 h-full bg-gradient-to-r from-[#B03052] to-[#D76C82] rounded-full transition-all duration-700 ease-out"
                      :style="{ width: `${goal.progress || 0}%` }"
                    />
                  </div>
                </div>
                
                <div class="flex flex-row mt-auto space-x-2">
                  <div v-if="goal.deadline" class="mt-auto">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M12 7V12L14.5 10.5M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>

                  <div v-if="goal.deadline" class="mt-auto">
                    <span v-if="(new Date(goal.deadline) - new Date()) > 86400000" class="text-gray-500">
                      {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60 * 24)) }} days left
                    </span>
                    <span v-else-if="(new Date(goal.deadline) - new Date()) > 0" class="text-red-700 font-semibold">
                      {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60)) }} hours left
                    </span>
                    <span v-else class="text-gray-500">
                      Deadline passed: {{ new Date(goal.deadline).toLocaleDateString() }}
                    </span>
                  </div>

                  <div class="flex flex-grow justify-end items-center mt-auto space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M3 10H21M7 3V5M17 3V5M6.2 21H17.8C18.9201 21 19.4802 21 19.908 20.782C20.2843 20.5903 20.5903 20.2843 20.782 19.908C21 19.4802 21 18.9201 21 17.8V8.2C21 7.07989 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V17.8C3 18.9201 3 19.4802 3.21799 19.908C3.40973 20.2843 3.71569 20.5903 4.09202 20.782C4.51984 21 5.07989 21 6.2 21Z" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span v-if="goal.deadline" class="text-gray-500">
                      {{ new Date(goal.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) }}
                    </span>
                    <span v-else class="text-gray-500 italic">No deadline</span>
                  </div>
                </div>
                
              </div>
              <div class="mb-2">
                <div v-if="goalToUpdate && goalToUpdate.id === goal.id">
                  <h4 class="mt-4 text-lg font-semibold">Update Current Episode</h4>
                  <div>
                    <label for="currentSeason">Season:</label>
                    <input type="number" id="currentSeason" v-model="goalToUpdate.season" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <div>
                    <label for="currentEpisode">Episode:</label>
                    <input type="number" id="currentEpisode" v-model="goalToUpdate.episode" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <button @click="updateGoal(goalToUpdate)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Save
                  </button>
                  <button @click="goalToUpdate = null" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Cancel
                  </button>
                </div>
              </div>
              <!-- Action Buttons -->
              <div class="flex gap-2 mt-4">
                <button
                  @click="toggleGoalCompletion(goal)"
                  :class="[
                    'flex-1 flex items-center justify-center px-4 py-2.5 rounded-xl font-medium transition-all duration-200',
                    goal.completed
                      ? 'bg-green-500 text-white hover:bg-green-600 shadow-lg shadow-green-500/25'
                      : 'bg-[#B03052] text-white hover:bg-[#8B2440] hover:text-white'
                  ]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M9 11L12 14L22 4M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C13.1257 3 14.1978 3.2284 15.1808 3.6358" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  {{ goal.completed ? 'Completed' : 'Complete' }}
                </button>
                
                <button
                  @click="openEditForm(goal)"
                  class="px-3 py-2.5 bg-white text-[#B03052] rounded-xl hover:bg-[#B03052] hover:text-white transition-all duration-200 border-2 border-[#B03052]"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M11 4H4C3.44772 4 3 4.44772 3 5V20C3 20.5523 3.44772 21 4 21H19C19.5523 21 20 20.5523 20 20V13M18.5 2.5C19.3284 1.67157 20.6716 1.67157 21.5 2.5C22.3284 3.32843 22.3284 4.67157 21.5 5.5L12 15L8 16L9 12L18.5 2.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                
                <button
                  @click="deleteGoal(goal.id)"
                  class="px-3 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M14 10V17M10 10V17M6 7V18C6 19.1046 6.89543 20 8 20H16C17.1046 20 18 19.1046 18 18V7M6 7H8M6 7H4M8 7V5C8 3.89543 8.89543 3 10 3H14C15.1046 3 16 3.89543 16 5V7M8 7H16M16 7H18M16 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No group goals found in this category.</p>
          </div>
        </div>

        <!-- Display Completed Goals -->
        <div v-if="showCompletedGoals" class="py-4">
          <div v-if="loadingGoals" class="flex justify-center items-center py-16">
            <div class="animate-bounce">
              <svg class="w-16 h-16 text-[#B03052]" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
              </svg>
            </div>
          </div>
          <div v-else-if="completedGoalsByCategory.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-6">
            <div v-for="goal in completedGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-6 flex flex-col min-h-[280px] border border-[#D76C82]/10 opacity-75">
              <div class="flex-grow flex flex-col overflow-hidden">
                <h3 class="text-xl font-bold text-gray-800 my-3 break-words">{{ goal.title }}</h3>
                <p class="text-gray-600 mb-3 break-words">{{ goal.description }}</p>
                <div v-if="goal.season && goal.episode" class="text-gray-600 mb-2">
                  Season: {{ goal.season }} Episode: {{ goal.episode }}
                </div>
                <div v-if="goal.group" class="text-sm text-[#B03052] font-semibold mb-2">Group: {{ goal.group.name }}</div>
                
                <div class="flex flex-row mt-auto space-x-2">
                  <div class="flex items-center space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M9 11L12 14L22 4M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C13.1257 3 14.1978 3.2284 15.1808 3.6358" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="text-green-600 font-semibold">Completed</span>
                  </div>
                  
                  <div class="flex flex-grow justify-end items-center mt-auto space-x-1">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" fill="none">
                      <path d="M3 10H21M7 3V5M17 3V5M6.2 21H17.8C18.9201 21 19.4802 21 19.908 20.782C20.2843 20.5903 20.5903 20.2843 20.782 19.908C21 19.4802 21 18.9201 21 17.8V8.2C21 7.07989 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V17.8C3 18.9201 3 19.4802 3.21799 19.908C3.40973 20.2843 3.71569 20.5903 4.09202 20.782C4.51984 21 5.07989 21 6.2 21Z" stroke="#a3a3a3" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span v-if="goal.deadline" class="text-gray-500">
                      {{ new Date(goal.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) }}
                    </span>
                    <span v-else class="text-gray-500 italic">No deadline</span>
                  </div>
                </div>
              </div>

              <!-- Action Buttons -->
              <div class="flex gap-2 mt-4">
                <button
                  @click="redoGoal(goal)"
                  class="flex-1 flex items-center justify-center px-4 py-2.5 rounded-xl font-medium transition-all duration-200 bg-green-600 text-white hover:bg-green-700 hover:text-white"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" fill="none">
                    <path d="M4 12V9C4 5.68629 6.68629 3 10 3H20M20 3L17 6M20 3L17 0M20 12V15C20 18.3137 17.3137 21 14 21H4M4 21L7 18M4 21L7 24" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Re-Do Goal
                </button>
                
                <button
                  @click="deleteGoal(goal.id)"
                  class="px-3 py-2.5 bg-white text-red-600 rounded-xl hover:bg-red-600 hover:text-white transition-all duration-200 border-2 border-red-600"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                    <path d="M14 10V17M10 10V17M6 7V18C6 19.1046 6.89543 20 8 20H16C17.1046 20 18 19.1046 18 18V7M6 7H8M6 7H4M8 7V5C8 3.89543 8.89543 3 10 3H14C15.1046 3 16 3.89543 16 5V7M8 7H16M16 7H18M16 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No completed goals found in this category.</p>
          </div>
        </div>
      </div>

      <!-- Edit Goal Modal -->
      <div v-if="showEditForm && editingGoal" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75 backdrop-blur-sm z-50">
        <div class="max-w-lg w-full p-6 bg-white rounded-lg shadow-md">
          <h2 class="text-2xl font-semibold mb-4 text-center">Edit Goal Progress</h2>
          <form @submit.prevent="updateGoal">
            
            <!-- Progress Slider -->
            <div class="mb-6">
              <label for="progress" class="block text-sm font-medium text-gray-700 mb-2">
                Progress: {{ editingGoal.progress }}%
              </label>
              <input 
                type="range" 
                id="progress" 
                v-model="editingGoal.progress" 
                min="0" 
                max="100" 
                step="5"
                class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
              />
              <div class="flex justify-between text-xs text-gray-600 mt-1">
                <span>0%</span>
                <span>25%</span>
                <span>50%</span>
                <span>75%</span>
                <span>100%</span>
              </div>
            </div>

            <!-- Deadline field -->
            <div class="mb-4">
              <label for="editDeadline" class="block text-sm font-medium text-gray-700 mb-1">Deadline:</label>
              <input
                type="datetime-local"
                id="editDeadline"
                v-model="editingGoal.deadline"
                class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
              />
              <p class="text-xs text-gray-500 mt-1">Leave empty to remove deadline</p>
            </div>

            <!-- Series-specific fields -->
            <div v-if="editingGoal.category === 'Series'" class="space-y-4">
              <div>
                <label for="editSeason" class="block text-sm font-medium text-gray-700 mb-1">Season:</label>
                <input
                  type="number"
                  id="editSeason"
                  v-model="editingGoal.season"
                  min="1"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
                />
              </div>
              <div>
                <label for="editEpisode" class="block text-sm font-medium text-gray-700 mb-1">Episode:</label>
                <input
                  type="number"
                  id="editEpisode"
                  v-model="editingGoal.episode"
                  min="1"
                  class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
                />
              </div>
            </div>

            <div class="flex justify-between space-x-2 mt-6">
              <button 
                type="submit" 
                class="bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg hover:bg-[#8B2440] transition duration-300"
              >
                Update Goal
              </button>
              <button 
                @click="closeEditForm" 
                type="button" 
                class="bg-gray-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-gray-700 transition duration-300"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Add Goal and Form -->
      <div v-if="showForm" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75 backdrop-blur-sm">
        <div class="max-w-lg w-full p-6 bg-white rounded-lg shadow-md">
          <h2 class="text-2xl font-semibold mb-4 text-center">Add Goal</h2>
          <form @submit.prevent="addGoal">
            <div class="mb-4 flex items-center justify-center">
              <div class="flex gap-4">
                <label class="inline-flex items-center">
                  <input 
                    type="radio" 
                    name="goalType"
                    v-model="goalType" 
                    value="personal"
                    class="form-radio" 
                  />
                  <span class="ml-2">Personal Goal</span>
                </label>
                <label v-if="userGroups.length > 0" class="inline-flex items-center">
                  <input 
                    type="radio" 
                    name="goalType"
                    v-model="goalType" 
                    value="group"
                    class="form-radio" 
                  />
                  <span class="ml-2">Group Goal</span>
                </label>
              </div>
            </div>

            <div v-if="goalType === 'group' && userGroups.length > 0" class="mb-4">
              <select v-model="selectedGroup" class="w-full p-2 border border-gray-300 rounded-lg">
                <option disabled value="">Select a Group</option>
                <option v-for="group in userGroups" :key="group.id" :value="group.id">{{ group.name }}</option>
              </select>
            </div>

            <div class="mb-4">
              <input v-model="title" type="text" placeholder="Goal Title" class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500" />
            </div>

            <div class="mb-4">
              <textarea v-model="description" placeholder="Description" class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"></textarea>
            </div>

            <div class="mb-4">
              <label for="category">Category:</label>
              <select v-model="category" id="category" class="w-full p-2 border border-gray-300 rounded-lg">
                <option disabled value="">Select a Category</option>
                <option v-for="category in goalCategories" :key="category" :value="category">{{ category }}</option>
              </select>
            </div>

            <div v-if="category === 'Series'" class="mb-4">
              <label for="season">Season:</label>
              <input type="number" id="season" v-model="season" class="w-full p-2 border border-gray-300 rounded-lg" />
            </div>

            <div v-if="category === 'Series'" class="mb-4">
              <label for="episode">Episode:</label>
              <input type="number" id="episode" v-model="episode" class="w-full p-2 border border-gray-300 rounded-lg" />
            </div>

            <div class="mb-4">
              <label for="deadline" class="block text-sm font-medium text-gray-700 mb-1">Deadline:</label>
              <input
                type="datetime-local"
                id="deadline"
                v-model="deadline"
                class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
              />
              <p class="text-xs text-gray-500 mt-1">Leave empty for no deadline</p>
            </div>

            <div class="flex justify-between space-x-2">
              <button type="submit" class="bg-green-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-green-700 transition duration-300">Add Goal</button>
              <button @click="showForm = false" type="button" class="bg-red-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-red-700 transition duration-300">Cancel</button>
            </div>

          </form>
        </div>
      </div>
    </section>
  </div>
  <div v-else class="text-center mt-10">
    <p>You must be logged in to access goals.</p>
    <router-link to="/login" class="text-blue-500">Log In</router-link>
  </div>
</template>


<script>
import { ref  } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';
import { useToast } from "vue-toastification";
import { eventBus } from '@/eventBus';


export default {
  setup() {
    const toast = useToast();
    return { toast };
  },
  
  props: {
    goal: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      dropdowns: ref({}),
      openGoalId: null,
      selectedGroup: '',
      showForm: false,
      showEditForm: false,
      editingGoal: null,
      showPersonalGoals: true,
      showGroupGoals: false,
      showCompletedGoals: false,
      title: '',
      description: '',
      deadline: '',
      goalType: 'personal',
      category: '',
      season: '',
      episode: '',
      goalToUpdate: null,
      userId: null,
      userGroups: [],
      groups: [],
      goals: [],
      loadingGoals: false,
      selectedCategory: 'All',
      goalCategories: [
        'All',
        'Books',
        'Coding',
        'Cooking',
        'Fitness',
        'Food and Dining',
        'Movies',
        'Series',
        'Music',
        'Photography',
        'Travel',
        'Other',
      ],
    };
  },

  computed: {
    isAuthenticated() {
      const store = useStore();
      return store.getters.isAuthenticated;
    },

    personalGoalsByCategory() {
      if(this.selectedCategory === 'All') {
        return this.goals.filter(
          (goal) =>
            !goal.is_group_goal &&
            !goal.completed &&
            goal.user_id === this.userId
        );
      }
      return this.goals.filter(
        (goal) =>
          !goal.is_group_goal &&
          goal.category === this.selectedCategory &&
          !goal.completed &&
          goal.user_id === this.userId
      );
    },

    groupGoalsByCategory() {
      if(this.selectedCategory === 'All') {
        return this.goals.filter(
          (goal) =>
            goal.is_group_goal &&
            !goal.completed &&
            this.userGroups.some((group) => group.id === goal.group_id)
        );
      }
      return this.goals.filter(
        (goal) =>
          goal.is_group_goal &&
          goal.category === this.selectedCategory &&
          !goal.completed &&
          this.userGroups.some((group) => group.id === goal.group_id)
      );
    },

    completedGoalsByCategory() {
      if(this.selectedCategory === 'All') {
        return this.goals.filter(
          (goal) =>
            goal.completed &&
            (this.userGroups.some((group) => group.id === goal.group_id) ||
              goal.user_id === this.userId)
        );
      }
      return this.goals.filter(
        (goal) =>
          goal.category === this.selectedCategory &&
          goal.completed &&
          (this.userGroups.some((group) => group.id === goal.group_id) ||
            goal.user_id === this.userId)
      );
    },
  },

  methods: {
    toggleDropdown(goalId) {
      this.openGoalId = this.openGoalId === goalId ? null : goalId;
    },

    redoGoal(goal) {
      const newGoal = {
        title: goal.title,
        description: goal.description,
        deadline: goal.deadline,
        is_group_goal: goal.is_group_goal,
        group_id: goal.group_id,
        category: goal.category,
        season: goal.season,
        episode: goal.episode,
      };
      axios.post('/goals', newGoal)
        .then(response => {
          this.goals.push(response.data);
          this.fetchGoals();
          this.toast.success('Goal re-added!');
        })
        .catch(error => {
          this.toast.error('Error re-adding goal.');
          console.error("Error redoing goal:", error);
        });
    },

    async toggleGoalCompletion(goal) {
      try {
        goal.completed = !goal.completed;
        await axios.put(`/goals/${goal.id}`, { completed: goal.completed });
        this.toast.success('Goal completed! Congratulations!');
      } catch (error) {
        this.toast.error('Error toggling goal completion.');
        console.error('Error toggling goal completion:', error);
      }
    },

    async deleteGoal(goalId) {
      try {
        await axios.delete(`/goals/${goalId}`);
        this.goals = this.goals.filter((goal) => goal.id !== goalId);
      } catch (error) {
        console.error('Error deleting goal:', error);
      }
    },

    showUpdateForm(goal) {
      this.goalToUpdate = { ...goal };
    },

    cancelUpdate() {
      this.goalToUpdate = null;
    },

    openEditForm(goal) {
      // Format deadline for datetime-local input if it exists
      let formattedDeadline = '';
      if (goal.deadline) {
        const date = new Date(goal.deadline);
        // Format to YYYY-MM-DDTHH:mm for datetime-local input
        formattedDeadline = date.toISOString().slice(0, 16);
      }

      this.editingGoal = {
        ...goal,
        progress: goal.progress !== undefined ? goal.progress : 0,
        season: goal.season || '',
        episode: goal.episode || '',
        deadline: formattedDeadline
      };
      console.log('Opening edit form for goal:', goal);
      console.log('Editing goal with deadline:', this.editingGoal.deadline);
      this.showEditForm = true;
    },

    closeEditForm() {
      this.showEditForm = false;
      this.editingGoal = null;
    },

    async updateGoal() {
      try {
        const updateData = {
          progress: parseInt(this.editingGoal.progress)
        };

        // Add deadline if provided, or set to null to remove it
        if (this.editingGoal.deadline) {
          // Convert datetime-local format to ISO string
          updateData.deadline = new Date(this.editingGoal.deadline).toISOString();
        } else {
          updateData.deadline = null;
        }

        if (this.editingGoal.category === 'Series') {
          updateData.season = parseInt(this.editingGoal.season) || this.editingGoal.season;
          updateData.episode = parseInt(this.editingGoal.episode) || this.editingGoal.episode;
        }

        console.log('Updating goal with data:', updateData);

        await axios.put(`/goals/${this.editingGoal.id}`, updateData);

        const goalIndex = this.goals.findIndex(g => g.id === this.editingGoal.id);
        if (goalIndex !== -1) {
          this.goals[goalIndex] = {
            ...this.goals[goalIndex],
            ...updateData,
            progress: updateData.progress,
            deadline: updateData.deadline
          };
        }

        this.toast.success('Goal updated successfully!');
        this.closeEditForm();
      } catch (error) {
        this.toast.error('Error updating goal: ' + (error.response?.data?.message || error.message));
        console.error('Error updating goal:', error);
      }
    },

    selectCategory(category) {
      this.selectedCategory = category;
    },

    async fetchUserDetails() {
      try {
        const response = await axios.get('/user');
        this.userId = response.data.id;
        this.userGroups = response.data.groups;
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    },

    async fetchGoals() {
      this.loadingGoals = true;
      try {
        const response = await axios.get('/goals');
        this.goals = response.data;
      } catch (error) {
        if (error.response?.status !== 401) {
          console.error('Error fetching goals:', error);
          this.toast.error('Error fetching goals.');
        }
        this.goals = [];
      } finally {
        this.loadingGoals = false;
      }
    },

    async fetchGroups() {
      try {
        const response = await axios.get('/groups');
        this.groups = response.data;
      } catch (error) {
        if (error.response?.status !== 401) {
          console.error('Error fetching groups:', error);
          this.toast.error('Error fetching groups.');
        }
        this.groups = [];
      }
    },

    clearForm() {
      this.title = '';
      this.description = '';
      this.deadline = '';
      this.selectedGroup = '';
      this.goalType = 'personal';
      this.category = '';
      this.season = '';
      this.episode = '';
    },
  },

  async mounted() {
    try {
      await this.fetchUserDetails();
      await this.fetchGoals();
      await this.fetchGroups();

      this.handleGoalAdded = () => {
        this.fetchGoals();
      };
      eventBus.on('goal-added', this.handleGoalAdded);
    } catch (error) {
      // Only show error if it's not an authentication issue
      if (error.response?.status !== 401) {
        this.toast.error('Error initializing goals view.');
        console.error('Error during component mount:', error);
      }
    }
  },
  
  unmounted() {
    if (this.handleGoalAdded) {
      eventBus.off('goal-added', this.handleGoalAdded);
    }
  },
};
</script>


<style scoped>
/* Add any specific styles you want for this component here */
.cursor-pointer {
  cursor: pointer;
}

.transition-transform {
  transition: transform 0.3s;
}

/* Custom slider styles */
.slider::-webkit-slider-thumb {
  appearance: none;
  width: 20px;
  height: 20px;
  background: #B03052;
  border-radius: 50%;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #B03052;
  border-radius: 50%;
  cursor: pointer;
  border: none;
}

.slider::-webkit-slider-runnable-track {
  background: linear-gradient(to right, #B03052 0%, #B03052 var(--progress), #e5e7eb var(--progress), #e5e7eb 100%);
}

/* Fallback for line-clamp if not supported */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Ensure word breaking for long text */
.break-words {
  word-wrap: break-word;
  overflow-wrap: break-word;
}
</style>