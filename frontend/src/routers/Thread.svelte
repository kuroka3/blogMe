<script>
    import date2time from '../lib/utils'
    import api from '../lib/api'

    export let params = {}
    let thread_id = params.thread_id
    let thread = {comments:[]}

    let username = ""
    let pwd = ""
    let comment_content = ""

    function get_thread() {
        api('get', '/api/thread/' + thread_id, {}, (json) => {
            thread = json
        })
    }

    get_thread()

    function post_thread_comment(event) {
        event.preventDefault()

        let url = '/api/comment/write/thread/' + thread_id
        let params = {
            username: username,
            pwd: pwd,
            content: comment_content
        }
        api('post', url, params, (json) => {
            comment_content = ''
            get_thread()
        })
    }
</script>

<div class="container my-3">
    <!-- 스레드 -->
    <h3 class="border-bottom py-2">{thread.title}</h3>
    {thread.username} | 
    <div class="badge bg-light text-dark p-2">{thread.date}</div>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{thread.content}</div>
        </div>
    </div>
    <!-- 댓글 목록 -->
    {#each thread.comments as comment}
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{comment.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {date2time(comment.date)}
                </div>
            </div>
        </div>
    </div>
    {/each}
    <!-- 답변 등록 -->
    <form method="post" class="my-3">
        <div class="mb-3">
            <textarea rows="10" bind:value={comment_content} class="form-control" />
        </div>
        <input type="submit" value="등록" class="btn btn-primary" on:click="{post_thread_comment}" />
    </form>
</div>