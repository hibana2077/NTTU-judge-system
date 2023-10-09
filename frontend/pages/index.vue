
<script setup>
// dark mode function
const colorMode = useColorMode()

const isDark = computed({
  get () {
    return colorMode.value === 'dark'
  },
  set () {
    colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
  }
})
// dark mode function end

// table of contents function
const columns = [
  {
    key: 'id',
    label: '#'
  },
  {
    key: 'title',
    label: 'Title'
  },
  {
    key: 'content',
    label: 'Content'
  },
  {
    key: 'author',
    label: 'Author'
  },
  {
    key: 'date',
    label: 'Date'
  },
  {
    key: 'action'
  }
]

const announcements = [{
  title: 'System Maintenance',
  content: 'The system will be down for maintenance on 2023-10-10 from 00:00 to 04:00 UTC.',
  author: 'Admin',
  date: '2023-10-05',
  action: '',
  id: 1
}, {
  title: 'New Features Added',
  content: 'We have updated the problem set interface for a better user experience.',
  author: 'DevTeam',
  date: '2023-09-25',
  action: '',
  id: 2
}, {
  title: 'Bug Fixes',
  content: 'We have fixed the login issues reported by some users.',
  author: 'SupportTeam',
  date: '2023-09-20',
  action: '',
  id: 3
}, {
  title: 'Contest Reminder',
  content: 'Monthly contest will be held on 2023-10-15. Prepare yourself!',
  author: 'ContestAdmin',
  date: '2023-10-01',
  action: '',
  id: 4
}, {
  title: 'Server Upgrade',
  content: 'We have upgraded our servers for faster problem submission evaluations.',
  author: 'DevOps',
  date: '2023-09-10',
  action: '',
  id: 5
}, {
  title: 'User Guide Updated',
  content: 'Check out the updated user guide for tips on how to improve your problem-solving skills.',
  author: 'TutorialTeam',
  date: '2023-08-30',
  action: '',
  id: 6
}]

const items = (row) => [
  [{
    label: 'Edit',
    icon: 'i-heroicons-pencil-square-20-solid',
    click: () => console.log('Edit', row.id)
  }, {
    label: 'Duplicate',
    icon: 'i-heroicons-document-duplicate-20-solid'
  }], [{
    label: 'Archive',
    icon: 'i-heroicons-archive-box-20-solid'
  }, {
    label: 'Move',
    icon: 'i-heroicons-arrow-right-circle-20-solid'
  }], [{
    label: 'Delete',
    icon: 'i-heroicons-trash-20-solid'
  }]
]

const show_detail = ref(false)
const show_detail_id = ref(0)
// table of contents function end

//toast function
const toast = useToast()
//toast function end
</script>

<template>
  <ClientOnly>
    <!-- nav bar -->
    <UContainer class="border-black-200 border-b-2 max-w-none">
      <nav class="flex justify-start items-center py-5 text-gray-600 border-slate-200 w-full">
        <ULink href="/" class="flex items-center space-x-2">
          <UImage
            src="/logo.png"
            alt="logo"
            width="40"
            height="40"
            class="rounded-full"
          />
          <span class="text-xl font-bold text-green-700">NTTUOJ</span>
        </ULink>
        <div class="flex-grow"></div>
        <div class="flex items-center space-x-2">
          <ULink to="/docs" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white">
            Docs
          </ULink>
          <ULink to="/components" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white">
            Problems
          </ULink>
          <ULink to="/examples" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white">
            Contests
          </ULink>
          <ULink to="/blog" class="px-3 py-2 rounded-md hover:bg-gray-700 hover:text-white">
            Status
          </ULink>
          <ULink to="login" class="px-3 py-2 rounded-3xl bg-green-700 text-white hover:bg-gray-700 hover:text-white">
            Login
          </ULink>
          <UButton
          :icon="isDark ? 'i-heroicons-moon-20-solid' : 'i-heroicons-sun-20-solid'"
          color="gray"
          variant="ghost"
          aria-label="Theme"
          @click="isDark = !isDark"
          />
        </div>
      </nav>
    </UContainer>
    <!-- table of contents **Announcements** -->
    <UContainer class="">
      <UCard class="m-10">
        <template #header>
          <div class="flex items-center justify-between">
            <h1 class="text-base font-semibold leading-6 text-primary-700">
              Announcements
            </h1>
            <UTooltip text="Refresh Announcements">
              <UButton color="gray" variant="ghost" icon="i-heroicons-arrow-path-20-solid" class="-my-1" @click="toast.add({ title: 'Announcements refreshed!' })" />
            </UTooltip>
          </div>
        </template>
        <UTable :rows="announcements" :columns="columns">
          <template #action-data="{ row }">
            <UDropdown :items="items(row)">
              <UButton color="gray" variant="ghost" icon="i-heroicons-ellipsis-horizontal-20-solid" />
            </UDropdown>
          </template>
          <!-- this is using for make content can be toggle -->
          <template #content-data="{ row }"> 
            <div class="flex items-center">
              {{ row.content }}
              <UButton
                color="gray"
                variant="ghost"
                icon="i-heroicons-document-text-20-solid"
                @click="show_detail = true; show_detail_id = announcements.findIndex(x => x.id === row.id); console.log(show_detail_id,show_detail,announcements.findIndex(x => x.id === row.id))"
              />
            </div>
          </template>
        </UTable>
      </UCard>
    </UContainer>
    <!-- table of contents **Announcements** end -->

    <UModal v-model="show_detail" prevent-close>
      <UCard v-if="show_detail" >
        <template #header class="flex justify-between items-center">
          <span class="text-xl font-bold text-green-700">{{ announcements[show_detail_id].title }}</span>
        </template>
        <span class="text-gray-600">{{ announcements[show_detail_id].content }}</span>
        <template #footer>
          <div class="flex justify-end">
            <UButton
              icon="i-heroicons-x-circle-20-solid"
              @click="show_detail = false;show_detail_id = 1;console.log(show_detail_id,show_detail)"
            >
              Close
            </UButton>
          </div>
        </template>
      </UCard>
    </UModal>

    <UNotifications icon="i-heroicons-check-circle"/>

    <!-- below block is for randering the content of the page -->
    <template #fallback>
        <div class="fixed inset-0 flex items-center justify-center">
            <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-primary-500"></div>
        </div>
    </template>
    <!-- end -->
  </ClientOnly>
</template>
