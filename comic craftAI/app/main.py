{% extends "base.html" %}

{% block title %}
ComicCraft — Create
{% endblock %}


{% block content %}

<section class="hero">

    <div>

        <p class="eyebrow">
            GEMINI + DIFFUSION
        </p>

        <h1>
            Turn your idea into a comic.
        </h1>

        <p class="hero-copy">

            Describe your story and ComicCraft
            creates five connected panels with
            narration, dialogue, illustrations
            and a downloadable PDF.

        </p>

    </div>

</section>


{% if demo_mode %}

<div class="notice">

    Demo mode is ON.

    The application can be tested without
    API keys.

    Set

    <code>
        DEMO_MODE=false
    </code>

    and add your API keys for real AI generation.

</div>

{% endif %}


<form

    class="card form-card"

    action="/generate"

    method="post"

    onsubmit="showLoading()"
>


<label>

    Story Prompt

    <textarea

        name="story_prompt"

        required

        maxlength="2000"

        placeholder="Example: A brave fox exploring an enchanted forest."
    >A brave fox exploring an enchanted forest.</textarea>

</label>


<div class="grid-2">


<label>

    Main Character Name

    <input

        name="character_name"

        value="Ravi"

        required

        maxlength="80"
    >

</label>


<label>

    Setting

    <select name="setting">

        <option>
            enchanted forest
        </option>

        <option>
            school
        </option>

        <option>
            space station
        </option>

        <option>
            futuristic city
        </option>

        <option>
            underwater kingdom
        </option>

    </select>

</label>


<label>

    Story Tone

    <select name="tone">

        <option>
            dramatic
        </option>

        <option>
            light-hearted
        </option>

        <option>
            funny
        </option>

        <option>
            poetic
        </option>

        <option>
            adventurous
        </option>

    </select>

</label>


<label>

    Art Style

    <select name="art_style">

        <option>
            comic book
        </option>

        <option>
            anime
        </option>

        <option>
            pixel art
        </option>

        <option>
            watercolor
        </option>

        <option>
            cinematic illustration
        </option>

    </select>

</label>


</div>


<button

    id="generate-button"

    class="button primary"

    type="submit"
>

    Create My Comic

</button>


<p
    id="loading"
    class="loading hidden"
>

    Creating your five-panel comic...

</p>


</form>


<section class="steps">

    <div>

        <strong>1</strong>

        <span>
            Outline
        </span>

    </div>


    <div>

        <strong>2</strong>

        <span>
            Story
        </span>

    </div>


    <div>

        <strong>3</strong>

        <span>
            Images
        </span>

    </div>


    <div>

        <strong>4</strong>

        <span>
            PDF
        </span>

    </div>

</section>

{% endblock %}