---
# the default layout is 'page'
icon: fa-solid fa-people-group
order: 2
media_subpath: /assets/posts/contributors
---

<style>

#panel-wrapper {
    display: none;
    width: 0;
}

#main-wrapper .container main {
    width: 100%;
}

/* ---- layout: responsive card grid ---- */
.contrib-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}

/* ---- card ---- */
.contrib-card {
  border: 1px solid rgba(0,0,0,.12);
  border-radius: 16px;
  overflow: hidden;
  background: var(--card-bg, #fff);
  box-shadow: rgba(0,0,0,.08) 0 2px 10px;
  display: flex;
  flex-direction: column;
}

/* title */
.contrib-card h2 {
  margin: 0;
  padding: .75rem 1rem .25rem;
  font-size: 1.2rem;
  font-weight: 500;
}

/* image: flush, square crop */
.contrib-card p:has(> img),
.contrib-card p:has(> a > img) {
  margin: 0;
  order: -1; /* move photo above the heading */
}

.contrib-card img {
  width: 100%;
  height: 220px;          /* pick your preferred height */
  object-fit: cover;      /* crops instead of stretching */
  display: block;
  border-radius: 12px;
}

/* bio collapsed/expanded */
.contrib-bio {
  overflow: hidden;
  padding: .25rem 1rem 0;
  font-size: 1rem;
  line-height: 1.5;
  flex: 1;
}

/* collapsed: clamp via max-height */
.contrib-card[data-collapsed="true"] .contrib-bio {
  max-height: 7.5em;
  position: relative;
}

/* fade uses card bg variable so it works in both light and dark mode */
.contrib-card[data-collapsed="true"] .contrib-bio::after {
  content: "";
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 2.5em;
  pointer-events: none;
  background: linear-gradient(transparent, var(--card-bg, #fff));
}

/* toggle button */
.contrib-toggle {
  margin-top: .4rem;
  padding: 0;
  border: none;
  background: none;
  cursor: pointer;
  font: inherit;
  font-size: 0.85rem;
  color: #777;
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.contrib-card:hover .contrib-toggle {
  opacity: 1;
}

.contrib-toggle:hover {
  text-decoration: underline;
}

.contrib-card.img-top img {
  object-position: center top;
}

.contrib-card:not(.img-top) img {
  object-position: center;
}

</style>


## Thomas C. Anderson

![Thomas C. Anderson](Anderson.jpg)

Anderson’s research, which draws upon both historical archival studies as well as plant biology and botany, explores how early modern colonial encounters with the natural world helped shape our modern pharmacopoeia.  
To the early modern naturalist and explorer, the keys to life’s greatest mysteries were to be found in the petals, leaves, and anthers of strange and exotic plants. Amerindian horticultural, botanical, and art-historical contributions to this complicated and multifaceted story have only recently emerged as a subject of scholarly interest. Anderson uses the history of medicine and botany to help elucidate the unknown pasts that have nonetheless had a major impact on the construction of scientific and medical knowledge up to today. Anderson is a master’s candidate at Columbia University. He holds a bachelor’s in history and French and Francophone Studies from Hamilton College. Anderson has explored transoceanic acclimatization and the indigenous Guanche pharmacopoeia in the Canary Islands; the early modern history of imperial science and medicine in Paris; ethnobotany and plant taxonomy at the New York Botanical Gardens; historical manuscripts concerning colonial plants and their uses at the John Carter Brown Library; and toxicity and plant defense systems at Cornell University. 

## Yota Batsaki
{: .img-top }

![Yota Batsaki](Bataski.jpg)

Yota Batsaki is the executive director of Dumbarton Oaks, a Harvard research institute, museum, and historic garden located in Washington, D.C. She is principal investigator of the Plant Humanities Initiative, undertaken in collaboration with JSTOR Labs and funded by the Andrew W. Mellon Foundation.  
The four-year initiative seeks to advance the emerging field of plant humanities in dialogue with the environmental humanities and with a focus on plant-human interactions. It encompasses the Plant Humanities Lab, an innovative digital space that supports the study of plants from the perspectives of the arts, sciences, and humanities. Related programming at Dumbarton Oaks includes fellowships, scholarly events, and a summer program that brings together students from various disciplines to explore the cultural histories of plants, learn digital skills, and contribute to the Plant Humanities Lab. Batsaki holds a PhD in comparative literature from Harvard University and coedited _The Botany of Empire in the Long Eighteenth Century_ (Dumbarton Oaks, 2016) with co-investigator Anatole Tchikine and Sarah Burke-Cahalan. She also co-curated with Tchikine the exhibition _Margaret Mee: Portraits of Plants_ in the Dumbarton Oaks museum.

## Camilo Uribe Botta
{: .img-top }

![Camilo Uribe Botta](Botta.jpg)

Uribe Botta’s current PhD research explores the orchid trade between Colombia and the United Kingdom in the nineteenth century, focusing on the global connections created around the plants on both sides of the Atlantic.  
His research analyzes the networks around these plants, from their hunting in the Colombian jungles to their conservation in British Botanical Gardens or collections from wealthy British collectors. Its overall aim is to chart the economic, scientific, and cultural conditions that led to the success of tropical orchids as a scientific and a commodity object. He focuses on the agency of orchids in global history and their relationship with humans in nineteenth-century commerce. Botta is a PhD candidate in history at the University of Warwick. He holds a bachelor’s and a master’s in history from Universidad de los Andes in Bogota, Colombia. Uribe Botta has been assistant curator and registrar and collections manager of the Museo Colonial and Museo Santa Clara, two public institutions that are part of the Ministry of Culture of Colombia. He participated in the overhaul and total renovation of the museum’s exhibitions between 2013 and 2019. He has been a history consultant for different cultural projects in museums, theaters, and television, including the Canoas Archeological Park in Soacha, the Teatro Colón de Bogotá, and Bolívar from Caracol TV and Netflix.

## Ashley Buchanan
{: .img-top }

![Ashley Buchanan](Buchanan_300x300.jpg)

Ashley Buchanan is the Postdoctoral Fellow for the Plant Humanities Initiative at Dumbarton Oaks. She is a historian of the early modern world, with a particular interest in plants, recipes, and medicinal cultures in seventeenth- and eighteenth-century Europe.   
She received her PhD in early modern history from the University of South Florida in December 2018. Her research spans many topics, which includes the history of science and medicine, women, and politics as well as the dynamics of gender and authority. Her current book project investigates the social, cultural, and political significance of pharmaceutical experimentation as well as the medicinal and botanical patronage at the late Medici Court (1650-1743). Her goal is to broaden the global dimension of recipes by studying the numerous exotic plants imported into Tuscany from the New World, East Africa, and Southeast Asia in the late 18th century. Ashley was a junior fellow in residence with the Medici Archive Project at the Archivio di Stato di Firenze and an Andrew W. Mellon Foundation Fellow at The Huntington.

## Elizabeth Chant
{: .img-top }

![Elizabeth Chant](Chant.jpg)

Elizabeth Chant is Teaching Fellow in Liberal Arts at the University of Warwick. Her research considers how nature has been understood in the Americas as an object to be consumed, with a special focus on visual culture.  
Liz works at the intersections of environmental history and cultural studies, and in her current project she is developing a comparative study of domestic tourism to industrial sites in former frontier territories in Argentina, Chile, and the U.S. during the first half of the twentieth century using maps and travel ephemera. Broadly, her research interests include map history, Latin American environmental history, the history of aesthetics and visual culture, and travel writing. Liz’s research has been supported by the UK Arts and Humanities Research Council, UK Society for Latin American Studies, and the ARTES Iberian and Latin American Visual Culture Group, and fellowships at the Library of Congress and Huntington Library. In 2022, she hosted an online workshop with Centre for Latin American and Caribbean Studies, University of London, to showcase ongoing work in Latin American plant humanities. 

## Verónica Matallana Chaves

![Verónica Matallana Chaves](Chaves.jpg)

Matallana Chaves’s undergraduate thesis research focuses on the history of textile work in Colombia and the use of natural fibers with a botanical-historical approach. Given the country’s sociocultural diversity, material cultural objects with an artisan trajectory play a key role in the consolidation of identities and symbolic networks.  
Although these objects have a consolidated historical trajectory, their agency has been changing as they have been touched by the dynamics of conservation, commodification, and resignification. Her work brings these points of tension and breakdowns in craft traditions to the surface. Chaves is in her third year of the undergraduate program in history at the Universidad Nacional de Colombia, where she has participated in projects on digital history, environmental history, and oral history and memory. She is currently part of the Public and Digital History group and is linked to the Laboratory of Historical Cartography and Digital History.

## Kira Bre Clingen
{: .img-top }

![Kira Bre Clingen](Clingen.jpg)

Kira Clingen is a Lecturer in Landscape Architecture at the Harvard Graduate School of Design, and a Research Associate at the Office for Urbanization. She is the project lead on Compound Vulnerabilities: The Case of Cape Ann, which uses scenario planning for climate change on the north shore of coastal Massachusetts.  
She holds a Masters in Landscape Architecture and Masters in Design Studies from Harvard, and a B.S. in Ecology and Evolutionary Biology and B.A. in Asian Studies and Environmental Policy from Rice University. She was awarded a 2016 Thomas J. Watson Fellowship to study climate change in Mauritius and Myanmar. Her current research focuses on climate literacy in landscape architecture, and climate change preparedness. 

## Ashley Thuthao Keng Dam

![Ashley Thuthao Keng Dam](Dam.jpg)

Ashley Thuthao Keng Dam (Ph.D. - they/them) is a medical anthropologist, ethnobotanist, and food writer living in the Netherlands. Thao is a multimodial mixed methods researcher who loves all things food, plants, and medicine.   
They completed the Plant Humanities Summer School Programme in 2021. Thao received their Ph.D. in Ecogastronomy, Education, and Society in 2022 from Università degli Studi di Scienze Gastronomiche (Pollenzo, Italy). They received their anthropological training from the University of Oxford (M.Sc., 2018, UK) and St. Mary's College of Maryland (B.A. Hons., 2016, USA). Currently, Thao works as a lecturer in Global Health in the Department of Health, Ethics, and Society (HES) at Maastricht University and is an Explorer for the National Geographic Society.

## Christina Emery

![Christina Emery](Emery.jpg)

Christina Emery is a senior undergraduate student majoring in archaeology and anthropology with a minor in history at the University of Cincinnati. She is pursuing certificates in Geographic Information Sciences, Mediterranean archaeology, and European Studies.  
Emery has archaeological field experience excavating a Fremont culture site in Boulder, Utah. She has also created multiple digital museum displays which revolve around the intersection of nature and science through medical discoveries from various cultures. Emery has conducted research into the ecology of and human interaction with the common dandelion, Taraxacum officinale. She has also conducted independent research into the influence that colonialism has had on the modern city of London. Her research interests currently consist of the changing relationships that people have with plants and the natural world.

## Katherine Enright
{: .img-top }

![Katherine Enright](Enright.jpg)

Katherine is a senior at Harvard College studying History and Anthropology. Her undergraduate thesis explores the history of colonial natural history collecting and illustration in 19th century Southeast Asia and the national politics behind the display of these artifacts in Singaporean museums today.  
She has a particular interest in the transformation of natural history into national heritage and in decolonial approaches to modern-day natural history collections. A bit further afield, her research interests also include Victorian plant horror fiction and the role of botany and botanic gardens in warfare. As a research assistant at Harvard's China Biographical Database Project, she has several years of digital humanities experience and hopes to apply digital tools to the study of 19th century natural history correspondence. At Harvard, she has also interned for the Harvard Museums of Science and Culture and the Fairbank Center for Chinese Studies, and was captain of Harvard Deepam, the college's classical Indian dance team. 

## Julia Fine

![Julia Fine](Julia_300x300.jpg)

Julia Fine is a graduate student at the University of Cambridge studying Modern South Asian Studies as a George Kingsley Roth and Cambridge Trust Scholar. She received her A.B. from Harvard University in History & Literature. In 2019, Julia was a fellow at the Folger Shakespeare Library, where she worked on the Mellon-funded "Before ‘Farm to Table’: Early Modern Foodways and Cultures" project.  
In 2020, she joined the Plant Humanities Initiative at Dumbarton Oaks, where she explored the movement of plants through the lens of imperial ambitions, specifically within the context of the Indian Ocean world.

## Rebecca Friedel
{: .img-top }

![Rebecca Friedel](Friedel_300x300.jpg)

Rebecca Friedel focuses on the cultural histories of plants from the Americas as a Plant Humanities Research Associate with Dumbarton Oaks. Friedel is also a paleoethnobotanist and PhD candidate in Anthropology at the University of Texas at San Antonio.  
Her doctoral research takes an interdisciplinary approach to reconstructing ancient Maya human-plant relationships. She is currently a U.S. Fulbright Scholar at the University of Belize where she is teaching under and establishing a BA program in Anthropology. She is passionate about education and improving access to knowledge more broadly, having co-founded an educational outreach 501c3 organization, Heritage Education Network Belize.

## Allison Fulton
{: .img-top }

![Allison Fulton](Fulton.jpg)

Allison Fulton is an English Ph.D. Candidate at the University of California Davis with a Designated Emphasis in Science and Technology Studies. Her dissertation examines how nineteenth-century American scientific disciplines were brought to form through gendered and racialized craftwork technologies.  
Recently, she participated in the residential course "Pioneers of Natural History" at the Oak Spring Garden Foundation and exhibited an artists’ book at the UC Davis Manetti Shrem Museum of Art Graduate Exhibition. Her work has been generously supported by the American Antiquarian Society and the Winterthur Library. 

## Kristan M. Hanson

![Kristan M. Hanson](Hanson_300x300.jpg)

Kristan M. Hanson is a Plant Humanities Fellow at Dumbarton Oaks. She is an art historian of nineteenth-century France, with a particular focus on depictions of women, ornamental plants, and spaces of horticultural labor and leisure.  
She received her PhD in art history from the University of Kansas in 2020. Her research interests include visual portrayals of plants and human-plant interactions; cultural associations of flowers and floral imagery with social markers of difference; horticultural trade networks, colonialism, and intimacy; and artistic engagements with environmental issues. Her dissertation applied digital humanities methods and tools to the study of horticultural art, plant mobility, and gendered spatial practices in the context of 1870s Paris. She has received fellowships and awards from the Oak Spring Garden Foundation, HASTAC Scholars program, and the Hall Center for the Humanities. Most recently, she coedited the exhibition catalogue _Perspectives on a Legacy Collection: Sallie Casey Thayer’s Gift to the University of Kansas_ (2020).

## Hannah Hardenbergh
{: .img-top }

![Hannah Hardenbergh](Hardenbergh.jpg)

Hannah Hardenbergh is a designer and artist from the Rocky Mountains of Colorado and attends the Harvard Graduate School of Design. Her work investigates how photography and image analysis frame collective imaginations of place, and the crucial social underpinnings that shape regional systems of water, soil, and plant communities.  
In her art practice, Hannah pushes the limitations of painting to represent abstractions of the human and non-human and has shown artwork at group exhibitions with SHIM Art Network in New York and Bridgeport, CT. Hannah holds a B.A. from Harvard College in History and Literature and will complete her master’s degree in landscape architecture at Harvard’s Graduate School of Design in 2025.

## Diana Heredia-López

![Diana Heredia-López](Heredia.jpg)

Diana Heredia-López is Ph.D. Candidate in the Department of History at the University of Texas at Austin. She holds a B.Sc. in Biology from the National Autonomous University of Mexico (UNAM). Originally trained as a biologist and historian of science, her guiding interests are the study and use of nature in Latin America and their repercussions on material culture and the environment.  
During her graduate studies she has explored different methodologies to incorporate new voices into global histories of science, commerce, and consumption. Diana’s dissertation project focuses on early colonial dye cultivation and its local producers and traders in Central and Southern Mexico. It explores the social and material culture implications of  large-scale dye cultivation for its producers and its connections to transatlantic commerce.  Her ongoing research has been funded by the Tinker Foundation, the Teresa Lozano Long Institute of Latin American Studies, and the Mellon Foundation.

## Rachel Hirsch
{: .img-top }

![Rachel Hirsch](hirsch.jpg)

What was it that made the gardens constructed throughout the Mughal Empire (1526–1857) such as Burhanpur’s Lal Bagh so appealing to these otherwise disgruntled travelers? What can we glean about their plant composition, function, and reception from textual, visual, and material sources? These and other related questions drive Hirsch’s current research on the art and architectural history of early modern South Asia.  
Her goal is to characterize perceptions of land and their relationship to the changing forms and functions of gardens in the sixteenth and seventeenth centuries. Ultimately, by underscoring the historical connections between humans, plants, and cultural production, she hopes to generate new understandings of territory in the early modern period.
Rachel Hirsch is a PhD candidate in history of art and architecture at Harvard University and a cultural historian of early modern South Asia. Her research interests include urban construction, perceptions of land and territory, garden history, and the potential for new art historical methods and sources. Her latest project took as its focus the Mughal city of Burhanpur and explored in depth its transformation through symbolic appropriation, ornamentation, and expansion along an underground water distribution system in the seventeenth century. She has also written extensively about Timurid and Mughal gardens and the role of travel writing in understandings of place.

## Christina Hourigan
{: .img-top }

![Christina Hourigan](Hourigan.jpg)

Christina Hourigan is a historical geography PhD candidate at Royal Holloway, University of London, in collaboration with the Royal Botanic Gardens, Kew. Her research on the history and value of the living collections and landscape of Kew's arboretum in the long nineteenth century is based in the plant humanities.  
She has a Masters in Garden History and a BSc in Plant Ecology, is the author of several books on trees and botanical history (as Christina Harrison), and was previously editor of RBG Kew's magazine for ten years. Her research interests include plant history, mobility and agency. She was part of the Dumbarton Oaks Plant Humanities Summer Programme in 2021 and has recently co-curated a new exhibition at RBG Kew (Uprooted) on archival stories of forest change with fellow DO alumnus Heather Craddock.

## Yao Jiang

![Yao Jiang](Jiang.jpg)

Jiang’s research explores the reinterpretation and reintroduction of the Chinese garden into modern discourse as a critical instrument to document China’s continuous cultural traditions. He is interested in the construction material exchanges and flows of the Chinese garden and its social and cultural relations, especially the introduction and cultivation of Chinese plants into the United States in the late twentieth century.  
For his thesis, Jiang is focusing on how the Astor Chinese Garden Court in the Metropolitan Museum of Art reshaped America’s understanding of the Chinese garden using several lenses, including the field of plant humanities. Jiang is a master student in architectural history at the University of Virginia. He holds a Bachelor of Art in environmental design from Tongji University. Jiang has served as the teaching assistant for the Sustainability Consciousness course at Tongji University (fall 2018) and the Metropolis course at UVA (spring 2020). He has recently been selected as a 2020 recipient of the Student Research Grant from the School of Architecture for his thesis project. Jiang is currently a part-time daily translator and editor to the ArchDaily China platform and serves as a research assistant to Andrew Johnston for his book project on preservation practice in China.

## Edyth Jostol
{: .img-top }

![Edyth Jostol](Jostol.jpg)

Edyth Jostol is a designer based in Seattle.  She received her Masters in Landscape Architecture from Harvard's Graduate School of Design, where her work focused on urban biodiversity, collective action and climate adaptation. She has previously worked at design firms in New York, Cambridge and DC, contributing to landscape projects of various scales. 

## Cati Kalinoski
{: .img-top }

![Cati Kalinoski](Kalinoski.jpg)

Kalinoski’s research examines plant-life exhibition work through the lens of performance to investigate theories of time, extinction, and the natural world. Her research is grounded on what we as humans can learn from plants and how they shape humans’ positions in the world.  
Taking from disciplines such as performance studies, anthropology, museum studies, environmental studies, and philosophy, Kalinoski’s work imagines a new form of politics around the lessons learned from nature. Kalinoski is a master candidate at New York University’s Tisch School of the Arts Performance Studies program and a theater practitioner. Her work is centered on plant studies and theories extinction through the lens of performance and exploring new notions of time in the Anthropocene. She has been awarded the Artist and Scholar Award for her research and has presented her work across the United States.

## Wouter Klein
{: .img-top }

![Wouter Klein](Klein_300x300.jpg)

Wouter Klein is Plant Humanities fellow at Dumbarton Oaks. A historian from the Netherlands, he received his PhD from Utrecht University in 2018. He is interested in the interconnected history of medicine, pharmacy, and botany in the early modern period; the circulation of knowledge and commodification processes of therapeutic drugs; and digital research methods to study medical practices of the past over the long term.  
He has a particular interest in the availability of materia medica in the past, either as commercial goods in trade records, research specimens for academic physicians, or commodified products for the general public. His research aims to unravel the question of how the global dimensions of commerce, science, and society helped some non-European natural substances become major commercial ingredients for medicines while others had much less success in the early modern medical marketplace. To tell those stories, his research makes use of large collections of digital historical data, like private correspondence, pharmaceutical manuals, auction records, and newspaper advertisements.

## W. John Kress
{: .img-top }

![W. John Kress](Kress_300x300.jpg)

W. John Kress is Distinguished Scientist and Curator Emeritus at the Smithsonian’s National Museum of Natural History and co-chair of the Earth BioGenome Project. He was curator of botany for over thirty years and formerly served as the interim undersecretary for science at the Smithsonian and director of science in the Grand Challenges Consortia. Kress received his BA from Harvard University and PhD from Duke University, where he studied tropical biology, ethnobotany, evolution, and ecology.  
He is a taxonomic specialist on the tropical Zingiberales, and his current research is focused on biodiversity genomics, conservation, and the Anthropocene. Among his more than 200 scientific and popular publications are his books _Plant Conservation: A Natural History Approach, The Weeping Goldsmith, The Art of Plant Evolution,_ and _The Ornaments of Life: Coevolution and Conservation in the Tropics._ His most recent book is _Living in the Anthropocene: Earth in the Age of Humans._ He is a fellow of the American Association for the Advancement of Science and is currently visiting scholar at Dartmouth College and the Arnold Arboretum of Harvard University. He lives in Dorset, Vermont.

## Anna Lawrence

![Anna Lawrence](Lawrence.jpg)

Lawrence’s research explores the sociopolitical lives of flowers in Victorian Britain, considering the different plant-human relations at play in the commodification of cut-flowers, botanical instruction for women and girls, domestic working-class floriculture, and settler colonial horticulture.  
Grounded theoretically in critical plant studies, Lawrence is interested in the material intimacies at play in these different spheres of plant-human interaction and how they were thought about at the time, seeking to illuminate a world of alternative and exaggerated sensibilities between people and plants to help us question our own approaches to plant nature today. Lawrence is a PhD student in the Department of Geography at the University of Cambridge where she also undertook her undergraduate and master’s degrees. She is a cultural and historical geographer interested in plant-human relationships. In addition to Victorian floriculture, she has worked on weeds and urban nature, as well as Caribbean music and culture in the United Kingdom. Anna currently co-convenes the graduate student-led research group Vegetal Epistemologies in Cambridge.

## Lucas Mertehikian

![Lucas Mertehikian](Mertehikian.jpg)

Mertehikian’s research offers a new lens on how to look at Latin American identity and its cultural and political relation with the United States with a focus on collecting efforts carried out by American scientists, diplomats, and scholars from the 1840s to the 1970s. Specifically, he analyzes three collections as case studies: Harvard University’s Latin American botanical collection, Dumbarton Oaks’s Pre-Columbian art collection, and Princeton University’s Latin American literary manuscripts collection.  
His current work examines how American botanist Asa Gray first took an interest in Latin American nature in the nineteenth century and the political implications that informed his collection of Latin American specimens. Mertehikian is a PhD candidate in Romance languages and literature at Harvard University. He holds a licenciatura in literature from the Universidad de Buenos Aires and a master’s in Latin American Studies from the Universidad Nacional de Tres de Febrero, both in Argentina. In 2018, he cocurated the exhibition Passports: Lives in Transit at Houghton Library, which was featured in the Boston Globe, the Harvard Gazette, and the Armenian Spectator, among other publications.

## Victoria Pickering

![Victoria Pickering](Pickering_300x300.jpg)

Dr. Victoria Pickering is a Research Associate in the Plant Humanities Initiative, having been a Research Fellow at Dumbarton Oaks  between 2019-2020. Previously, she researched the global movement of plants from the late seventeenth century onward at the British Museum and the Natural History Museum in London. Today, she continues to explore the collection, description, management, and use of natural history objects in the early modern period.

## Haley Price
{: .img-top }

![Haley Price](Haley.jpg)

Haley Price is a History Ph.D. student at Brown University and the Digital Humanities Specialist for UT Austin’s JapanLab. She studied History and Humanities as an undergraduate at UT Austin, where she engineered her own interdisciplinary degree plan to create educational history-based video games. This study culminated in The Pazzi Conspiracy, which aims to teach students about patronage and power in 15th-century Florence.  
Price is interested in the relationship between power, piety, and patronage in renaissance Italy as well as making history education more accessible through interactive digital media. She was a Summer Plant Humanities fellow at Dumbarton Oaks in 2021.

## Daisy Reid
{: .img-top }

![Daisy Reid](Reid.jpg)

Daisy Reid is a graduate student in comparative literature at the University of Southern California, with a research focus on contemporary speculative and ecological fictions in conversation with critical race, queer, and feminist theory.  
She holds a BA in French and Italian from University College London and an MA in comparative literature from the University of Amsterdam. Her current work explores literary and artistic representations of plant-being as they come to bear upon (bio)political structures surrounding gender, sexuality, erotics, and desire.

## Sierra Roark

![Sierra Roark](Roark.jpeg)

Sierra Roark is a doctoral candidate in the Department of Anthropology at the University of North Carolina at Chapel Hill, where she studies human-plant entanglements.  
Her dissertation "Green Gold: Plant Use, Identity, and Power in the Colonial Chesapeake, 1600-1800" examines archaeobotanical and historical evidence of plant use among the diverse populations living in the Tidewater region of Virginia and Maryland in the 17th- and 18th-centuries. Using a framework of well-being, Roark's research explores cultural exchange, ecological knowledge, foodways, medicinal strategies, land management, and the emergence of colonial botany. Roark holds an MA in Anthropology from the University of North Carolina at Chapel Hill and a BA in History and Anthropology from the University of Tennessee, Knoxville.

## Amara Santiesteban Serrano

![Amara Santiesteban Serrano](Serrano.jpg)

Amara Santiesteban is a biologist specializing in botany from the Autonomous University of Madrid (Spain). She holds an MSc in Tropical Biodiversity and Conservation, where she entered the world of Plant Humanities by studying the expedition of the XVIII century naturalist Alexander von Humboldt to the Canary Islands (Spain).  
Santiesteban was also granted during this period a JAE Intro fellowship at the Royal Botanical Garden of Madrid, where she was given the opportunity to untangle the complex taxonomy of the tropical plant family of the Brazil nut (Bertholletia excelsa, Lecythidaceae). Currently, she has been awarded a Ph.D. contract to conduct her research on the effects of wildfires on mycorrhizal fungi and their impact on plants, but she is determined to keep on working on a multidisciplinary approach of plant sciences where the local knowledge, art, literature, and naturalism walk side by side. The Dumbarton Oaks Summer Program provided the perfect ground for this young researcher to take off in this new stage of her academic career.

## Elaine Savory

![Elaine Savory](Savory.jpg)

Elaine Savory, Phd., is Emeritus Professor, Literary Studies and Environmental Studies, New School University, New York City. She has published widely on Caribbean and African literatures and most recently in environmental humanities, focusing on plants.

## John R. Schaefer
{: .img-top }

![John R. Schaefer](Schaefer.jpg)

John R. Schaefer is currently a U.S. Fulbright Scholar studying environmental education at Western Sydney University, with a focus on the cultural histories of native Australian flora.  
He is particularly interested in the interdisciplinary application of plants as teaching tools in conservation, ecology, and evolutionary biology at cultural heritage institutions, as well as increasing engagement with both archival and living plant collections through the digital humanities. John received his Bachelor of Arts from Harvard University in History and Science, focusing on the history of botany. His postgraduate research in Digital Humanities at the University of Cambridge examined the use of machine learning models in citizen science and humanities projects at the Royal Botanic Gardens, Kew. John joined the Plant Humanities Initiative at Dumbarton Oaks in 2021, where he explored transatlantic networks of knowledge exchange surrounding carnivorous plants.

## Jeannette Schollaert
{: .img-top }

![Jeannette Schollaert](Schollaert.jpg)

Jeannette Schollaert is a doctoral candidate in English at the University of Maryland, College Park. Her dissertation, tentatively titled "From Censors to Shouts: Ecologies of Abortion in American Fiction," traces the literary history of herbal abortifacients in relation to emerging medical technologies in American fiction from the nineteenth century to the present.  
She holds a BA in English and Women’s Studies from Chatham University in Pittsburgh, PA and an MA in English with a specialization in Women’s and Gender Studies from the University of Nebraska-Lincoln.

## Melinda Susanto
{: .img-top }

![Melinda Susanto](Susanto.jpg)

Susanto’s research investigates the practices of health and medicine in eighteenth-century Indonesia through the records of the Dutch East India Company. She is focusing on the utility of plants and indigenous knowledge from the archipelago, particularly the role of local intermediaries in facilitating European knowledge production of the region.  
Susanto is a PhD candidate in history at Leiden University. She completed an MA in colonial and global history at Leiden University in 2019. Prior to this, she worked as an assistant curator at the National Gallery Singapore between 2014 and 2018. Her previous projects have explored visual materials reflecting interactions between Europe and Southeast Asia, including works on paper and books produced as a result of European scientific explorations of the region. Susanto also holds an MA in the history of art from the Courtauld Institute of Art and a BA in art history and Ancient Greek from the Australian National University.

## Anatole Tchikine
{: .img-top }

![Anatole Tchikine](Tchikine_300x300.jpg)

Anatole Tchikine is curator of rare books at Dumbarton Oaks. An architectural historian and a specialist on early modern Italy, he holds a PhD from the University of Dublin, Trinity College. His work mainly addresses the intersections of art and science, including the history of fountain design, botanical gardens, and collecting and representations of nature.  
He is the author, with Pierre de la Ruffinière du Prey, of _"Discrizione della Villa Pliniana": Reimagining Antiquity in the Landscape of Umbria_ (2021), editor of _The Three Natures: Gardens and Landscapes of the Italian Renaissance_ (forthcoming), and coeditor of _The Botany of Empire in the Long Eighteenth Century_ (2016) and _Military Landscapes_ (2021).

## Matthew Turetsky
{: .img-top }

![Matthew Turetsky](Turetsky.jpg)

Matthew Turetsky is a Ph.D. student in History at Carnegie Mellon University studying Latin American and environmental history. His research focuses on the history of biodiversity conservation, cuisine, and food sovereignty in the Andes. He uses quinoa as a case study to understand the promotion, production, and consumption of traditional Andean crops in twentieth-century Peru and Bolivia. In 2023, he participated in the Plant Humanities Summer Program at Dumbarton Oaks.

## May Wang
{: .img-top }

![May Wang](Wang.jpg)

May Wang graduated from Harvard College in 2020 with a degree in comparative literature and a secondary in astrophysics. Her undergraduate work often focused on the intersection of cultural and scientific history, especially in nineteenth-century novels. Wang has interned at the Harvard Art Museums, Dumbarton Oaks, and the Smithsonian Astrophysical Observatory. Wang is currently a Postgraduate Writing and Reporting Fellow at Dumabrton Oaks.

<script>
document.addEventListener('DOMContentLoaded', () => {
  const root = document.querySelector('.page-content') || document.querySelector('article') || document.body;

  const grid = document.createElement('div');
  grid.className = 'contrib-grid';
  root.appendChild(grid);

  const h2s = Array.from(root.querySelectorAll('h2'));
  if (!h2s.length) return;

  h2s.forEach((h2) => {
    if (h2.closest('.contrib-card')) return;

    const card = document.createElement('section');
    card.className = 'contrib-card';
    card.dataset.collapsed = 'true';
    if (h2.classList.length) {
    card.classList.add(...h2.classList);
    }

    grid.appendChild(card);
    
    let node = h2;
    while (node) {
      const next = node.nextSibling;
      card.appendChild(node);

      const nextEl = next && next.nodeType === 1 ? next : null;
      if (nextEl && nextEl.tagName === 'H2') break;

      node = next;
    }

    const imageP = card.querySelector('p:has(> img)') || card.querySelector('p img')?.closest('p');
    const bioWrap = document.createElement('div');
    bioWrap.className = 'contrib-bio';

    let start = imageP ? imageP.nextSibling : card.querySelector('h2')?.nextSibling;
    while (start) {
      const next = start.nextSibling;
      if (!(start.nodeType === 1 && start.classList.contains('contrib-toggle'))) {
        bioWrap.appendChild(start);
      }
      start = next;
    }
    card.appendChild(bioWrap);

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'contrib-toggle';
    btn.setAttribute('aria-expanded', 'false');
    btn.textContent = 'More';
    card.appendChild(btn);

    btn.addEventListener('click', () => {
      const collapsed = card.dataset.collapsed === 'true';
      card.dataset.collapsed = collapsed ? 'false' : 'true';
      btn.setAttribute('aria-expanded', collapsed ? 'true' : 'false');
      btn.textContent = collapsed ? 'Less' : 'More';
    });
  });

  requestAnimationFrame(() => {
    grid.querySelectorAll('.contrib-card').forEach(card => {
      const bio = card.querySelector('.contrib-bio');
      const btn = card.querySelector('.contrib-toggle');
      if (bio && btn && bio.scrollHeight <= bio.clientHeight + 2) {
        btn.style.display = 'none';
        card.dataset.collapsed = 'false';
      }
    });
  });
});
</script>