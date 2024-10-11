<template>
  <div class="home-view flex flex-col items-center justify-start min-h-screen pt-14">
    <header class="text-center mb-8">
      <h1 class="text-6xl font-extrabold text-gray-800">Set Your Goals, Share Your Journey</h1>
      <p class="text-gray-500 mt-4 text-xl">
        Join a community of goal-setters and achievers. Create, track, and share your dreams with others.
      </p>
    </header>

    
    <button v-if="!isAuthenticated" class=" bg-gray-800 text-white py-3 px-8 rounded-lg shadow-md hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg">
      Join GoalBond Now!
    </button>
    <div v-if="isAuthenticated" class=" flex space-x-4">
      <button @click="goToGoals" class="bg-gray-800 text-white py-3 px-6 rounded-lg shadow-md hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg">
        Check Goals
      </button>
      <button @click="goToGroups" class="bg-gray-800 text-white py-3 px-6 rounded-lg shadow-md hover:bg-indigo-700 transition-all duration-300 ease-in-out text-lg">
        Check Groups
      </button>
    </div>

    <div class="relative w-full max-w-8xl flex items-center justify-center mt-12 pb-16">
      <div class="flex justify-center items-center overflow-hidden">
        <div
          v-for="(card, index) in cards"
          :key="index"
          class="w-80 h-80 rounded-lg border-4 border-white flex items-center justify-center m-2 relative"
          :style="{
            backgroundImage: `url(${card.image})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            opacity: index === activeCard ? 1 : 0.5,
            transform: index === activeCard ? 'scale(1.1)' : 'scale(0.9)',
            transition: 'opacity 0.3s ease, transform 0.3s ease',
            zIndex: index === activeCard ? 10 : 1
          }"
        >
          <div class="absolute inset-0 bg-black bg-opacity-30 flex items-center justify-center rounded-lg">
            <span class="text-white text-2xl font-bold">{{ card.text }}</span>
          </div>
        </div>
      </div>
    </div>

    <section class="feature-highlights w-full">
      <h2 class="text-4xl font-bold text-gray-800 text-center my-14">Why GoalBond?</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mx-14 my-16">
        <div class="feature-card bg-white shadow-lg rounded-lg overflow-hidden flex flex-col hover:shadow-xl transition-shadow duration-300">
          <div class="bg-gray-800 p-4 rounded-t-lg">
            <h1 class="text-xl font-semibold text-white">Personalised Goal Setting</h1>
          </div>
          <p class="text-gray-600 px-4 py-2 ">Easily set, track, and visualise your goals to keep yourself motivated.</p>
        </div>
        <div class="feature-card bg-white shadow-lg rounded-lg overflow-hidden flex flex-col hover:shadow-xl transition-shadow duration-300">
          <div class="bg-gray-800 p-4 rounded-t-lg">
            <h1 class="text-xl font-semibold text-white">Collaborative Goal Sharing</h1>
          </div>
          <p class="text-gray-600 px-4 py-2 ">Collaborate with friends and loved ones to create shared goals for experiences you want to enjoy together—whether it’s places to visit, shows to watch, or meals to try. Strengthen your bonds by exploring new adventures and savoring life’s moments side by side!</p>
        </div>
        <div class="feature-card bg-white shadow-lg rounded-lg overflow-hidden flex flex-col hover:shadow-xl transition-shadow duration-300">
          <div class="bg-gray-800 p-4 rounded-t-lg">
            <h1 class="text-xl font-semibold text-white">Celebrating Achievements</h1>
          </div>
          <p class="text-gray-600 px-4 py-2 ">Every achievement deserves recognition! Add pictures and reflections to completed goals, allowing you to celebrate your journey and inspire others.</p>
        </div>
      </div>
    </section>

    <section class="testimonials my-2 px-14">
      <h2 class="text-4xl font-bold text-gray-800 text-center my-16">What Our Users Say</h2>
      <div class="grid grid-cols-2 gap-6 mb-16">
        <div class="bg-white shadow-lg rounded-lg p-6">
          <p class="text-gray-600 italic">"GoalBond helped me achieve my travel goals! I finally visited Paris!"</p>
          <p class="text-gray-800 font-semibold">- Sarah T.</p>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-6">
          <p class="text-gray-600 italic">"The collaborative features made planning with friends so easy and fun!"</p>
          <p class="text-gray-800 font-semibold">- John D.</p>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-6">
          <p class="text-gray-600 italic">"I was able to finally complete my bucket list thanks to GoalBond!"</p>
          <p class="text-gray-800 font-semibold">- Emily W.</p>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-6">
          <p class="text-gray-600 italic">"GoalBond is a great tool for keeping track of goals and progress. I love it!"</p>
          <p class="text-gray-800 font-semibold">- David M.</p>
        </div>
      </div>
    </section>


  </div>
</template>

<script>
import { computed, ref, onMounted, onBeforeUnmount } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'; 

export default {
  name: 'HomeView',
  setup() {
    const store = useStore();
    const router = useRouter();

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || '');

    const activeCard = ref(0);
    const cards = [
      { image: "https://plus.unsplash.com/premium_photo-1667030474693-6d0632f97029?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", text: "Achieve Your Goals" },
      { image: "https://plus.unsplash.com/premium_photo-1677101626318-422def4d9b8b?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", text: "Success Awaits" },
      { image: "https://plus.unsplash.com/premium_photo-1677545182425-4fb12bdb9faf?q=80&w=2672&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", text: "Dream Big" },
      { image: "https://plus.unsplash.com/premium_photo-1661729755480-4fdb5105b53e?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", text: "Meow Meow"},
      { image: "https://plus.unsplash.com/premium_photo-1664299749481-ac8dc8b49754?q=80&w=2669&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", text: "Lock In"},
    ];

    const goToGoals = () => {
      router.push('/goals');
    };

    const goToGroups = () => {
      router.push('/groups');
    };

    const nextCard = () => {
      activeCard.value = (activeCard.value + 1) % cards.length;
    };

    const prevCard = () => {
      activeCard.value = (activeCard.value - 1 + cards.length) % cards.length;
    };

    // Autoplay feature
    let autoplayInterval;
    const startAutoplay = () => {
      autoplayInterval = setInterval(nextCard, 3000); // Change card every 3 seconds
    };

    const stopAutoplay = () => {
      clearInterval(autoplayInterval);
    };

    // Start autoplay on mounted and stop on unmounted
    onMounted(startAutoplay);
    onBeforeUnmount(stopAutoplay);

    return {
      isAuthenticated,
      username,
      goToGoals,
      goToGroups,
      activeCard,
      cards,
      nextCard,
      prevCard,
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
