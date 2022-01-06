def add_entity_to_doc(doc, ent):
        try:
            doc.ents = list(doc.ents)+[ent]
        except Exception as e:
            #Look for colliding entities
            print(f"Unhandled exception: {ent.text}")
            pass