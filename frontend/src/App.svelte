<script>
  async function root() {
    const res = await fetch('http://127.0.0.1:8000/');
    const json = await res.json();

    if (res.ok) {
      return json.message;
    } else {
      alert('error');
    }
  }

  let promise = root();
</script>

{#await promise}
  <p>...waiting</p>
{:then message}
  <h1>{message}</h1>
{/await}