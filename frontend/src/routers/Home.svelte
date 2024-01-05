<script>
    import date2time from '../lib/utils'
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

<div class='container my-3'>
    <table class='table'>
        <thead>
        <tr class='table-dark'>
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
            <th>조회수</th>
            <th>추천</th>
        </tr>
        </thead>
        
        <tbody>
            {#each thread_list as thread, i}
            <tr>
                <td>{thread.id}</td>
                <td>
                    <a use:link href='/thread/{thread.id}'>{thread.title}</a>
                </td>
                <td>{date2time(thread.date)}</td>
                <td>{thread.view}</td>
                <td>{thread.like - thread.unlike}</td>
            </tr>
            {/each}
        </tbody>
    </table>
</div>