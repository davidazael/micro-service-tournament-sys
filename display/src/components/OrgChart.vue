<template>
  <div class="layout-content">
    <div class="content-section implementation">
      <div class="card">
        <h5>Advanced</h5>
        <OrganizationChart
          :value="data1"
          :collapsible="true"
          class="company"
          selectionMode="single"
          v-model:selectionKeys="selection"
          @nodeSelect="onNodeSelect"
          @nodeUnselect="onNodeUnselect"
          @nodeCollapse="onNodeCollapse"
          @nodeExpand="onNodeExpand"
        >
          <template #person="slotProps">
            <div class="node-header ui-corner-top">
              {{ slotProps.node.data.label }}
            </div>
            <div class="node-content">
              <img :src="'/assets/' + slotProps.node.data.avatar" width="32" />
              <div>{{ slotProps.node.data.name }}</div>
            </div>
          </template>
          <template #default="slotProps">
            <span>{{ slotProps.node.data.label }}</span>
          </template>
        </OrganizationChart>
      </div>

      <div class="card">
        <h5>Basic</h5>
        <OrganizationChart :value="data2">
          <template #default="slotProps">
            <span>{{ slotProps.node.data.label }}</span>
          </template>
        </OrganizationChart>
      </div>
    </div>
  </div>
</template>

<script>
import { useToast } from 'primevue/usetoast'
import { ref } from 'vue'
import OrganizationChart from 'primevue/organizationchart'

export default {
  components: {
    OrganizationChart,
  },
  setup() {
    const data1 = ref({
      key: '0',
      type: 'person',
      styleClass: 'p-person',
      data: {
        label: 'CEO',
        name: 'Walter White',
        avatar: 'walter.jpg',
      },
      children: [
        {
          key: '0_0',
          type: 'person',
          styleClass: 'p-person',
          data: { label: 'CFO', name: 'Saul Goodman', avatar: 'saul.jpg' },
          children: [
            {
              key: '0_0_0',
              data: { label: 'Tax' },
              selectable: false,
              styleClass: 'department-cfo',
            },
            {
              key: '0_0_1',
              data: { label: 'Legal' },
              selectable: false,
              styleClass: 'department-cfo',
            },
          ],
        },
        {
          key: '0_1',
          type: 'person',
          styleClass: 'p-person',
          data: { label: 'COO', name: 'Mike E.', avatar: 'mike.jpg' },
          children: [
            {
              key: '0_1_0',
              data: { label: 'Operations' },
              selectable: false,
              styleClass: 'department-coo',
            },
          ],
        },
        {
          key: '0_2',
          type: 'person',
          styleClass: 'p-person',
          data: { label: 'CTO', name: 'Jesse Pinkman', avatar: 'jesse.jpg' },
          children: [
            {
              key: '0_2_0',
              data: { label: 'Development' },
              selectable: false,
              styleClass: 'department-cto',
              children: [
                {
                  key: '0_2_0_0',
                  data: { label: 'Analysis' },
                  selectable: false,
                  styleClass: 'department-cto',
                },
                {
                  key: '0_2_0_1',
                  data: { label: 'Front End' },
                  selectable: false,
                  styleClass: 'department-cto',
                },
                {
                  key: '0_2_0_2',
                  data: { label: 'Back End' },
                  selectable: false,
                  styleClass: 'department-cto',
                },
              ],
            },
            {
              key: '0_2_1',
              data: { label: 'QA' },
              selectable: false,
              styleClass: 'department-cto',
            },
            {
              key: '0_2_2',
              data: { label: 'R&D' },
              selectable: false,
              styleClass: 'department-cto',
            },
          ],
        },
      ],
    })

    const data2 = ref({
      key: '0',
      data: { label: 'F.C. Barcelona' },
      children: [
        {
          key: '0_0',
          data: { label: 'F.C. Barcelona' },
          children: [
            {
              key: '0_0_0',
              data: { label: 'Chelsea F.C.' },
            },
            {
              key: '0_0_1',
              data: { label: 'F.C. Barcelona' },
            },
          ],
        },
        {
          key: '0_1',
          data: { label: 'Real Madrid' },
          children: [
            {
              key: '0_1_0',
              data: { label: 'Bayern Munich' },
            },
            {
              key: '0_1_1',
              data: { label: 'Real Madrid' },
            },
          ],
        },
      ],
    })
    const selection = ref({})
    const posts = ref(
      {
        key: '0',
        data: { label: 'F.C. Barcelona' },
        children: [
          {
            key: '0_0_0',
            data: { label: 'Chelsea F.C.' },
          },
          {
            key: '0_0_1',
            data: { label: 'F.C. Barcelona' },
          },
        ],
      },
      {
        key: '0_1',
        data: { label: 'Real Madrid' },
        children: [
          {
            key: '0_1_0',
            data: { label: 'Bayern Munich' },
          },
          {
            key: '0_1_1',
            data: { label: 'Real Madrid' },
          },
        ],
      }
    )

    console.log(posts)
    console.log(data1)

    const toast = useToast()

    const onNodeSelect = node => {
      toast.add({
        severity: 'success',
        summary: 'Node Selected',
        detail: node.data.label,
        life: 1000,
      })
    }

    const onNodeUnselect = node => {
      toast.add({
        severity: 'success',
        summary: 'Node Unselected',
        detail: node.data.label,
        life: 1000,
      })
    }
    const onNodeExpand = node => {
      toast.add({
        severity: 'success',
        summary: 'Node Expanded',
        detail: node.data.label,
        life: 1000,
      })
    }

    const onNodeCollapse = node => {
      toast.add({
        severity: 'success',
        summary: 'Node Collapsed',
        detail: node.data.label,
        life: 1000,
      })
    }

    return {
      toast,
      posts,
      data1,
      data2,
      selection,
      onNodeSelect,
      onNodeUnselect,
      onNodeExpand,
      onNodeCollapse,
    }
  },
}

// function onNodeSelect(node) {
//   console.log(node)
//   toast.add({
//     severity: 'success',
//     summary: 'Node Selected',
//     detail: node.data.label,
//     life: 3000,
//   })
// }

// function onNodeUnselect(node) {}
// function onNodeExpand(node) {}
// function onNodeCollapse(node) {}
</script>

<style scoped lang="scss">
::v-deep(.p-organizationchart) {
  .p-person {
    padding: 0;
    border: 0 none;
  }

  .node-header,
  .node-content {
    padding: 0.5em 0.7rem;
  }

  .node-header {
    background-color: #495ebb;
    color: #ffffff;
  }

  .node-content {
    text-align: center;
    border: 1px solid #495ebb;
  }

  .node-content img {
    border-radius: 50%;
  }

  .department-cfo {
    background-color: #7247bc;
    color: #ffffff;
  }

  .department-coo {
    background-color: #a534b6;
    color: #ffffff;
  }

  .department-cto {
    background-color: #e9286f;
    color: #ffffff;
  }
}
</style>
