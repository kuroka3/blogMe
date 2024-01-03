<script>
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

<h1>{thread.title}</h1>

<div>
    {thread.content}
</div>

<div>
    {thread.like}:{thread.unlike}
</div>

<ul>
    {#each thread.comments as comment}
        <li>{comment.content} | {comment.like}:{comment.unlike}</li>
    {/each}
</ul>

<form method='post'>
    <input type='text' bind:value={username} placeholder='닉네임'>
    <input type='password' bind:value={pwd} placeholder='비밀번호'>
    <textarea rows='15' bind:value={comment_content}></textarea>
    <input type='submit' value='등록' on:click="{post_thread_comment}">
</form>

<style>
    input[type=text], input[type=password] {
        width:45%;
        margin-left: 1%;
        margin-right: 1%;
    }
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }    
</style>