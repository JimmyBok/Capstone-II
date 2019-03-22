Patent Citation Networks: A Graph Theory Representation

## Motivation:

###### To gain a better understanding of the patent citation network and provide starter tools for others to analyze the patent citation network
---
#### Background

Despite the 'common knowledge' that they are a flawed measure, patents are commonly used in economic research as a proxy variable for measuring technological progress over time.

*What are Patents*:
Patents are mechanisms for individuals, companies, or governments to legally “own” ideas. The United States Patent Office (USPO) states that a granted patent gives the patent owner **“the right to exclude others from making, using, offering for sale, or selling”** an idea or process for 20 years after the patent is granted, thus creating a legal monopoly over the implementation of an idea. However, that monopoly must be enforced by the patent filer not the patent office.

*Why do we have Patents*:
Patents are meant to encourage economic innovation through increasing investment in research, encouraging companies to share ideas instead of keeping "trade secrets," and protecting the rights for humans to benefit from "the product of his/her mind." This rational sounds great in theory, but are they what we see in practice today.

---
#### Problem: Cracks in the System

Enter the "Patent Troll"

![Patent Troll](https://github.com/JimmyBok/Capstone-II/images/Patent_troll.jpg)

Definition: _"A company that obtains the rights to one or more patents in order to profit by means of licensing or litigation, rather than by producing its own goods or services."_

Instead of producing economic good patent troll's will buy patents from companies who need to liquidate assets, then turn around to other companies and demand royalties under threat of an expensive lawsuit.

Cracks like this tell me we should look further into Patents in order to encourage our societal growth.

 ---

### Data
The data I used for this project was provided by The National Bureau of Economic Research and fully described in the paper bellow.

_Hall, B. H., A. B. Jaffe, and M. Trajtenberg (2001). "The NBER Patent Citation Data File: Lessons, Insights and Methodological Tools." NBER Working Paper 8498._

My data set consisted of just under 3 million Utility Patents granted by the USPO between the years of 1963 and 1999, and the patent numbers cited by those 3 million Utility Patents consisting of over 16 million patent citation links. The Utility Patents are categorically split from over 400 official patent classes into constructed variables of 6 categories and 36 subcategories. This was provided by Jaffe, and Trajtenberg (2001).

The 6 Categories
1) Chemical
2) Computers and Communications
3) Drugs and Medical
4) Electrical and Electronics
5) Mechanical
6) Others

*Utility patents*: may be granted to anyone who invents or discovers any new and useful process, machine, article of manufacture, or composition of matter, or any new and useful improvement thereof;

---
### Exploratory Data Analysis (EDA)

##### Patents by Year by Category
![Count of Patents by Year by Category](https://github.com/JimmyBok/Capstone-II/images/patent_count_year.jpg)

##### Average Number of Patent Citation by Year by Category

![Patents Citation Average by Year by Category](https://github.com/JimmyBok/Capstone-II/images/Average_citation_year.jpg)


#### Not all SubCategories follow the trend

![SubCategory Patent Count](https://github.com/JimmyBok/Capstone-II/images/SubCategory Patent Count.jpg)

---

## Graphs

#### Genetically Modified Animals

![Graph of Patent degrees removed](https://github.com/JimmyBok/Capstone-II/images/Genetics_graph.jpg)



#### Categories citing across categories

![Category Citations](https://github.com/JimmyBok/Capstone-II/images/Category_citations.jpg)


---
### Summary



---
### Future Work
-Utilizing more advanced software for displaying graphs
-Create a better dashboard for others to analyze patents of interest
-Look into how companies react when trying to "box out" competition
-Look into effects on a subcategory network of patent expiration
