<script>
    import api from '../lib/api'
    import { link } from 'svelte-spa-router'

    let thread_list = []

    function get_thread_list() {
        api('get', '/api/thread/list', {}, (json) => {
        thread_list = json
        })
    }

    get_thread_list()
</script>

<ul>
    {#each thread_list as thread}
        <li><a use:link href='/thread/{thread.id}'>{thread.title}</a></li>
    {/each}
</ul>