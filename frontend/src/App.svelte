<script>
  import Router from 'svelte-spa-router'
  import Home from './routers/Home.svelte'
  import Thread from './routers/Thread.svelte'

  const routes = {
    '/': Home,
    '/thread/:thread_id': Thread
  }
</script>

<Router {routes}/>