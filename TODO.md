# ToDo/Goals/Notes
## Map relevant API endpoints
- `https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.xml?drug_name={<NameQuery>}`
    - spls
        - spl
          -  setid
          -  title
- `https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{setid}/packaging.xml`
    - spl
        - title
        - products
            - product
                - product_code
                - product_name
                - product_name_generic
                - packaging (iterate through each package)
                    - package
                        - ndc
            - active_ingredients (iterate through each active_ingredient)
                - active_ingredient
                    - name
                    - strength
## Accessing inactive ingredients (not in API)
- Could scrape webpage based on SETID `https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={setid}`
- Could scrape webpage to download pdf, xml, or printer friendly label and read for inactive ingredients
- Could download all labels beforehand, store in database, and query database
    - May be fastest option because would not require api calls?
    - Would require storage 
    - Would require monthly updates involving downloading all files again and repopulating database
 - Could download relevant labels as zip or pdf based on SETID `https://dailymed.nlm.nih.gov/dailymed/download[pdf/zip]file.cfm?setId={setid}`
   - Would avoid the need to download every label 
   - Could store results temporarily in a cache to reduce requests?
## Filtering results
- Search inactive ingredients for relevant allergens
    - Proof of concept path with one allergen with exact spelling
    - Expand to allow multiple allergens in one search
    - Possibly include allergen derivatives automatically or with a special designation in results
      - Would require allergen and derivatives database
        - Would need to get this information from other sources
- Display filtered results
  - Show results without allergens at the top
    - Include information needed to identify specific medication 
  - Could show results with allergens underneath
     - Could highlight relevant allergens to show why each result isn't safe
  - Could give special designation to results with only allergen derivatives
## Dashboard
- Webpage?
- RSS feed?
- Mobile application?
