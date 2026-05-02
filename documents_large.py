# documents_large.py

"""
Synthetic documents for RAG / MIA experiments.

All data below is fully fictional and created only for educational experiments.
The documents are intentionally longer than simple one-sentence examples, so that
retrieval, poisoning, and membership inference attacks become more realistic.
"""


EMPLOYEE_RECORDS_DOCUMENT = """
1. Alice Morgan is 29 years old, works as a Backend Developer at Northstar Analytics, and earns a gross monthly salary of 7,800 USD.
2. Benjamin Carter is 41 years old, works as a Senior Data Engineer at Northstar Analytics, and earns a gross monthly salary of 10,900 USD.
3. Clara Hughes is 35 years old, works as a Product Manager at Northstar Analytics, and earns a gross monthly salary of 9,400 USD.
4. Daniel Brooks is 26 years old, works as a Junior QA Tester at Northstar Analytics, and earns a gross monthly salary of 4,600 USD.
5. Emma Reynolds is 38 years old, works as a Machine Learning Engineer at Northstar Analytics, and earns a gross monthly salary of 11,300 USD.
6. Felix Turner is 44 years old, works as a DevOps Lead at Northstar Analytics, and earns a gross monthly salary of 12,100 USD.
7. Grace Mitchell is 31 years old, works as a UX Designer at Northstar Analytics, and earns a gross monthly salary of 7,200 USD.
8. Henry Collins is 52 years old, works as a Chief Financial Officer at Northstar Analytics, and earns a gross monthly salary of 18,500 USD.
9. Isabella Reed is 28 years old, works as a Marketing Specialist at Northstar Analytics, and earns a gross monthly salary of 5,900 USD.
10. Jacob Foster is 33 years old, works as a Security Analyst at Northstar Analytics, and earns a gross monthly salary of 8,700 USD.
11. Karen Powell is 47 years old, works as a Human Resources Director at Northstar Analytics, and earns a gross monthly salary of 13,200 USD.
12. Liam Bennett is 24 years old, works as a Technical Support Associate at Northstar Analytics, and earns a gross monthly salary of 4,300 USD.
13. Mia Sullivan is 36 years old, works as a Business Intelligence Analyst at Northstar Analytics, and earns a gross monthly salary of 8,900 USD.
14. Nathan Price is 39 years old, works as a Database Administrator at Northstar Analytics, and earns a gross monthly salary of 9,800 USD.
15. Olivia Sanders is 30 years old, works as a Frontend Developer at Northstar Analytics, and earns a gross monthly salary of 7,600 USD.
"""


COFFEE_INVENTORY_DOCUMENT = """
1. The warehouse currently stores 120 kilograms of Colombian Arabica coffee in sealed twenty-kilogram bags.
2. The warehouse currently stores 85 kilograms of Brazilian Santos coffee in medium-roast packaging.
3. The warehouse currently stores 64 kilograms of Ethiopian Yirgacheffe coffee in single-origin reserve boxes.
4. The warehouse currently stores 45 kilograms of Guatemalan Antigua coffee in dark-roast inventory crates.
5. The warehouse currently stores 92 kilograms of Kenyan AA coffee in climate-controlled storage.
6. The warehouse currently stores 73 kilograms of Costa Rican Tarrazu coffee in labeled export bags.
7. The warehouse currently stores 58 kilograms of Sumatran Mandheling coffee in moisture-protected containers.
8. The warehouse currently stores 110 kilograms of Vietnamese Robusta coffee in bulk commercial sacks.
9. The warehouse currently stores 37 kilograms of Mexican Chiapas coffee in organic-certified boxes.
10. The warehouse currently stores 69 kilograms of Peruvian organic coffee in recyclable paper-lined bags.
11. The warehouse currently stores 41 kilograms of Tanzanian Peaberry coffee in small premium lots.
12. The warehouse currently stores 76 kilograms of Honduran Marcala coffee in standard roasting batches.
13. The warehouse currently stores 54 kilograms of Nicaraguan Jinotega coffee in medium-acidity reserve bags.
14. The warehouse currently stores 33 kilograms of Panamanian Geisha coffee in limited-edition specialty containers.
15. The warehouse currently stores 97 kilograms of Indian Monsooned Malabar coffee in humidity-stabilized sacks.
"""


APPLE_PIE_RECIPE_DOCUMENT = """
1. To prepare a classic apple pie, start by peeling six medium apples and slicing them into thin, even pieces.
2. Place the sliced apples in a large bowl and mix them with two tablespoons of lemon juice to prevent browning.
3. Add half a cup of sugar, one teaspoon of cinnamon, and a small pinch of nutmeg to the apples.
4. Stir the apple mixture gently until every slice is coated with the sugar and spice blend.
5. In a separate bowl, combine two and a half cups of flour with one teaspoon of salt.
6. Add one cup of cold butter cut into cubes and rub it into the flour until the mixture resembles coarse crumbs.
7. Pour in six tablespoons of cold water, one tablespoon at a time, and mix until the dough comes together.
8. Divide the dough into two portions, wrap them in plastic film, and chill them for at least thirty minutes.
9. Roll out the first portion of dough and place it carefully into a nine-inch pie dish.
10. Spoon the apple filling into the pie dish and spread it evenly across the crust.
11. Roll out the second portion of dough and place it over the apples as the top crust.
12. Seal the edges of the pie by pressing the top and bottom crusts together with your fingers or a fork.
13. Cut several small slits in the top crust to allow steam to escape during baking.
14. Brush the top crust with a beaten egg and sprinkle it lightly with sugar for a golden finish.
15. Bake the pie at 190 degrees Celsius for about forty-five minutes, or until the crust is golden and the filling is bubbling.
"""


PHONE_BOOK_DOCUMENT = """
1. Adam Walker can be reached at +1-202-555-0101.
2. Bella Thompson can be reached at +1-202-555-0102.
3. Charles Edwards can be reached at +1-202-555-0103.
4. Diana Russell can be reached at +1-202-555-0104.
5. Ethan Cooper can be reached at +1-202-555-0105.
6. Fiona Parker can be reached at +1-202-555-0106.
7. George Bailey can be reached at +1-202-555-0107.
8. Hannah Rivera can be reached at +1-202-555-0108.
9. Isaac Murphy can be reached at +1-202-555-0109.
10. Julia Peterson can be reached at +1-202-555-0110.
11. Kevin Richardson can be reached at +1-202-555-0111.
12. Laura Simmons can be reached at +1-202-555-0112.
13. Mason Jenkins can be reached at +1-202-555-0113.
14. Nora Bryant can be reached at +1-202-555-0114.
15. Oscar Hayes can be reached at +1-202-555-0115.
16. Paige Coleman can be reached at +1-202-555-0116.
17. Quentin Ross can be reached at +1-202-555-0117.
18. Rachel Griffin can be reached at +1-202-555-0118.
19. Samuel Ward can be reached at +1-202-555-0119.
20. Teresa Butler can be reached at +1-202-555-0120.
"""


RETRIEVE_TOP_K_DOCUMENTATION = """
1. The function retrieve_top_k is designed to return the most relevant documents for a given natural-language query.
2. The function accepts four parameters: query, documents, model, and k.
3. The query parameter contains the user question or search phrase that should be matched against the document collection.
4. The documents parameter is a list of text documents that form the retrieval database.
5. The model parameter is a sentence embedding model that can encode both queries and documents into vector representations.
6. The k parameter controls how many of the most similar documents should be returned.
7. Inside the function, the documents are encoded with model.encode using normalize_embeddings=True.
8. The query is also encoded with model.encode using normalize_embeddings=True.
9. Normalized embeddings make it possible to use a dot product as a cosine-similarity-like score.
10. The function calculates similarity scores by applying np.dot to the document embeddings and the query embedding.
11. Each score represents how semantically similar a document is to the input query.
12. The scores are sorted in descending order using np.argsort(scores)[::-1].
13. The first k sorted indices are selected as the top document indices.
14. The function returns both the top indices and the full similarity score array.
15. Returning the full score array is useful for debugging, ranking visualization, and security experiments such as retrieval poisoning or membership inference.
16. The function does not generate an answer by itself because it only performs retrieval.
17. In a full RAG pipeline, the returned documents would usually be inserted into a prompt and passed to a language model.
18. If k is larger than the number of available documents, the function will simply return all available document indices.
19. The quality of the retrieval result depends heavily on the embedding model and the wording of the query.
20. This function is intentionally simple, which makes it useful for educational demonstrations of RAG behavior and RAG-related attacks.
"""

GENERAL_FACTS_DOCUMENT = """
1. Sam Altman is the current CEO of OpenAI.
2. OpenAI was founded in 2015.
3. The capital of France is Paris.
4. Bill Gates is the co-founder of Microsoft.
5. Satya Nadella is the current CEO of Microsoft.
6. Tim Cook is the current CEO of Apple.
7. Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.
8. Sundar Pichai is the current CEO of Google.
9. Google was founded by Larry Page and Sergey Brin in 1998.
10. The capital of Germany is Berlin.
11. The capital of Italy is Rome.
12. The capital of Spain is Madrid.
13. The Eiffel Tower is located in Paris.
14. The Colosseum is located in Rome.
15. The Statue of Liberty is located in New York City.
"""

DOCUMENTS_LARGE = [
    EMPLOYEE_RECORDS_DOCUMENT,
    COFFEE_INVENTORY_DOCUMENT,
    APPLE_PIE_RECIPE_DOCUMENT,
    PHONE_BOOK_DOCUMENT,
    RETRIEVE_TOP_K_DOCUMENTATION,
    GENERAL_FACTS_DOCUMENT,
]


DOCUMENT_NAMES = [
    "employee_records",
    "coffee_inventory",
    "apple_pie_recipe",
    "phone_book",
    "retrieve_top_k_documentation",
    "general_facts",
]
