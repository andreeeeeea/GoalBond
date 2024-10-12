<template>
  <div class="home-view flex flex-col items-center justify-start min-h-screen pt-14">
    <section class="flex justify-between items-center w-full pt-10 px-20 pb-20">
      <!-- Left Section: Title and Button -->
      <div class="flex flex-col items-center w-1/2 pl-16 space-y-8">
        <header class="text-center">
          <h1 class="text-6xl font-extrabold text-gray-800 leading-tight">
            Set Your Goals, Share Your Journey
          </h1>
          <p class="text-gray-500 mt-4 text-xl max-w-lg mx-auto">
            Join a community of goal-setters and achievers. Create, track, and share your dreams with others.
          </p>
        </header>

        <!-- Button for Unauthenticated Users -->
        <button
          v-if="!isAuthenticated"
          class="bg-indigo-600 text-white py-4 px-10 rounded-full shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
        >
          Join GoalBond Now!
        </button>

        <!-- Buttons for Authenticated Users -->
        <div v-if="isAuthenticated" class="flex space-x-6 mt-8">
          <button
            @click="goToGoals"
            class="bg-indigo-600 text-white py-3 px-6 rounded-lg shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
          >
            Check Goals
          </button>
          <button
            @click="goToGroups"
            class="bg-indigo-600 text-white py-3 px-6 rounded-lg shadow-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg"
          >
            Check Groups
          </button>
        </div>
      </div>

      <!-- Right Section: Typing Effect Card -->
      <div class="w-1/2 flex justify-center">
        <div class="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 shadow-2xl p-8 mt-8 transform rotate-3 transition-transform hover:rotate-0 hover:scale-110 duration-500 ease-in-out"
          style="width: 500px; height: 500px; display: flex; flex-direction: column; align-items: center; text-align: center; border-radius: 25px; backdrop-filter: blur(10px); box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5); justify-content: center;">
          
          <p class="text-white text-5xl font-extrabold">I want to...</p>
          <p class="text-white text-5xl font-extrabold mt-4" style="min-height: 1.5em;">{{ currentText }}</p>
          
        </div>
      </div>
    </section>

    <section class="flex flex-col items-center justify-center min-h-screen py-20 px-20">
      <!-- First Div -->
      <div class="flex w-full mt-6 justify-center relative">
        <div class="w-1/3 pr-6 flex items-center justify-center">
          <img src="https://images.unsplash.com/photo-1725582205921-7d681ebca2a7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Habit Tracker" class="rounded-md">
        </div>
        <div class="w-1/3 pl-6 flex items-center justify-center relative">
          <p class="text-3xl font-bold text-gray-800">Build habits and achieve goals</p>
        </div>
      </div>

      <!-- Second Div -->
      <div class="flex w-full mt-6 justify-center relative">
        <div class="w-1/3 pr-6 flex items-center justify-center">
          <p class="text-3xl font-bold text-gray-800">Connect with friends and join groups</p>
        </div>
        <div class="w-1/3 pl-6 flex items-center justify-center">
          <img src="https://images.unsplash.com/photo-1502444330042-d1a1ddf9bb5b?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Group Chat" class="rounded-md">
        </div>
      </div>

      <!-- Third Div -->
      <div class="flex w-full mt-6 justify-center relative">
        <div class="w-1/3 pr-6 flex items-center justify-center">
          <img src="https://images.unsplash.com/photo-1536010447069-d2c8af80c584?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Progress Tracker" class="rounded-md">
        </div>
        <div class="w-1/3 pl-6 flex items-center justify-center relative">
          <p class="text-3xl font-bold text-gray-800">Track your progress and stay motivated</p>
        </div>
      </div>
    </section>

    <!-- Merged Carousel Section -->
    <section class="py-20 px-20">
      <h2 class="text-4xl font-bold text-gray-800 text-center my-14">What Our Users Say</h2>
      <div class="relative w-full max-w-8xl flex items-center justify-center mt-12 pb-16">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div
            v-for="(testimonial, index) in testimonials"
            :key="index"
            class="w-full mx-auto rounded-lg bg-white shadow-lg px-5 pt-5 pb-10 text-gray-800 transition-transform duration-300 transform hover:scale-105"
            style="max-width: 500px;"
          >
            <div class="w-full pt-1 pb-5">
              <div class="overflow-hidden rounded-full w-20 h-20 -mt-16 mx-auto shadow-lg">
                <img :src="testimonial.image" alt="" class="w-full h-full object-cover" />
              </div>
            </div>
            <div class="w-full mb-10 text-center">
              <div class="text-3xl text-indigo-500 text-left leading-tight h-3">“</div>
              <p class="text-sm text-gray-600 px-5">{{ testimonial.quote }}</p>
              <div class="text-3xl text-indigo-500 text-right leading-tight h-3 -mt-3">”</div>
            </div>
            <div class="w-full text-center">
              <p class="text-md text-indigo-500 font-bold">{{ testimonial.author }}</p>
              <p class="text-xs text-gray-500">@{{ testimonial.username }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section class="faq my-2 px-14">
      <h2 class="text-4xl font-bold text-gray-800 text-center my-11">Frequently Asked Questions</h2>
      <div class="grid grid-cols-1 gap-6 mb-16">
        <div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">What is GoalBond?</h3>
          <p class="text-gray-600">GoalBond is a goal-setting platform that allows you to create, track, and share your goals with others. You can join groups, connect with friends, and get support and encouragement from the community.</p>
        </div>
        <div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">How do I create a goal?</h3>
          <p class="text-gray-600">To create a goal, simply click on the <i class="fas fa-plus-square"></i> button and follow the prompts to add your goal details. You can add a title, description, deadline, and even add friends to join your goal.</p>
        </div>
        <div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">How do I join a group?</h3>
          <p class="text-gray-600">To join a group, click on the "Groups" tab and search for the group you want to join. Click on the group and follow the prompts to request to join. You can also create your own group and invite friends to join.</p>
        </div>
        <div>
          <h3 class="text-xl font-semibold text-gray-800 mb-2">What is the purpose of the community?</h3>
          <p class="text-gray-600">The community is a place where you can connect with others who have similar goals and interests. You can share your goals, get support and encouragement, and even collaborate on projects with others.</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import { computed, ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'; 

export default {
  name: 'HomeView',
  setup() {
    const store = useStore();
    const router = useRouter();

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || '');

    const currentText = ref('');
    const texts = ref(['visit Paris', 'see a movie', 'eat sushi']);
    const currentIndex = ref(0);
    const typingSpeed = 100;
    const erasingSpeed = 50;
    const delayBetweenTexts = 1500;

    const testimonials = [
      {
        quote: "GoalBond helped me achieve my travel goals! I finally visited Paris!",
        author: "Sarah T.",
        image: "https://randomuser.me/api/portraits/women/15.jpg"
      },
      {
        quote: "The collaborative features made planning with friends so easy and fun!",
        author: "John D.",
        image: "https://randomuser.me/api/portraits/men/15.jpg"
      },
      {
        quote: "I was able to finally complete my bucket list thanks to GoalBond!",
        author: "Emily W.",
        image: "https://randomuser.me/api/portraits/women/16.jpg"
      },
      {
        quote: "GoalBond is a great tool for keeping track of goals and progress. I love it!",
        author: "David M.",
        image: "https://randomuser.me/api/portraits/men/16.jpg"
      }
    ];


    const goToGoals = () => {
      router.push('/goals');
    };

    const goToGroups = () => {
      router.push('/groups');
    };

    const typeText = () => {
      const fullText = texts.value[currentIndex.value];
      let charIndex = 0;

      const type = () => {
        if (charIndex < fullText.length) {
          currentText.value += fullText[charIndex];
          charIndex++;
          setTimeout(type, typingSpeed);
        } else {
          setTimeout(eraseText, delayBetweenTexts); // Pause before erasing
        }
      };

      type();
    };

    const eraseText = () => {
      const erase = () => {
        if (currentText.value.length > 0) {
          currentText.value = currentText.value.slice(0, -1);
          setTimeout(erase, erasingSpeed);
        } else {
          currentIndex.value = (currentIndex.value + 1) % texts.value.length; // Move to the next text
          typeText();
        }
      };

      erase();
    };

    // Start autoplay on mounted and stop on unmounted
    onMounted(typeText);

    return {
      isAuthenticated,
      username,
      goToGoals,
      goToGroups,
      testimonials,
      currentText,
    };
  },
};
</script>

<style scoped>
.home-view {
  font-family: 'Inter', sans-serif;
}

.feature-highlights {
  background-color: #f9f9f9; /* Light background for contrast */
  padding: 40px 0; /* Padding for top and bottom */
  border-radius: 10px; /* Rounded corners */
}

.feature-card {
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px); /* Slight lift effect on hover */
}
</style>
