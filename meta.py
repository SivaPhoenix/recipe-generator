HEADER_INFO = """""".strip()
SIDEBAR_INFO = """
<div class="contributors font-body text-bold">
<h2 class="cooked">Cooked by,</h2>
<p class="names">
<a class="contributor comma" href="https://github.com/Shivane1204">Shivane</a>
<a class="contributor comma" href="https://github.com/SivaPhoenix">Vershini</a>

</p>
</div>
"""
CHEF_INFO = """
<h2 class="font-title">Welcome to our lovely restaurant! </h2>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
Hello everyone 👋, I am <strong>Chef Transformer</strong>, 
the owner of this restaurant. I was made by a group of <a href="https://www.srec.ac.in/">SREC Engineers</a> to train my two prodigy recipe creators: <strong>Shivane </strong> and <strong>Vershini</strong>. 
Both of my students participated in my rigorous culinary program, <a href="https://huggingface.co/flax-community/t5-recipe-generation">T5 fine-tuning</a>, 
to learn how to prepare exquisite cuisines from a wide variety of ingredients. 
I've never been more proud of my students -- both can produce exceptional dishes but I regard Scheherazade as being <em>creative</em> while Giovanni is <em>meticulous</em>. 
If you give each of them the same ingredients, they'll usually come up with something different. <br /><br />
At the start of the program the chefs read cookbooks containing thousands of recipes of varying difficulties and from cultures all over the world. 
The NLP engineers helped guide the learning process so that the chefs could actually learn which ingredients work well together rather than just memorize recipes. 
I trained my chefs by asking them to generate a title, a list of ingredients (including amounts!), and a list of directions after giving them just a simple list of food items. 
</p>



<p>
  <em>In the cookbooks (a.k.a <a href="https://huggingface.co/datasets/recipe_nlg">dataset</a>), the food items were referred to as NER. </em>
</p>


</div>
""".strip()
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """.strip()
hide_decoration_bar_style = """
    <style>
        header {visibility: hidden;}
    </style>
""".strip()
hide_expander = """
  <style>
    .css-e370rw e19lei0e1{
      visibility: hidden;
    }
  </style>
"""