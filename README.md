# GenVillages
Procedural Village Generation using μ + λ mutation principles

We implement the μ + λ mutation strategy to generate village spaces. Each space generated comprises naturally occurring terrain types such as mountains, forests and waterbodies as well as buildings ranging from houses and schools to hospitals and shrines. The exact physical location of each of these ‘components’ in space is decided by the output of the evolutionary algorithm.

We empirically found μ=30 and λ=10 to perform the best for our implementation. A relatively large μ is expected since variety in the setting of natural terrain types can only be introduced via randomly generated individuals in initial population: these components do not go through any mutation as new offspring are generated. Only the vectors containing other component types go through mutation. And to make the maps more surreal, the natural terrain types randomly occur in two to four clumps rather than appearing completely at random like other types.

To execute, please follow the following steps:
1. Install the software 'Processing' from https://processing.org/. 
2. Clone the project to your local file system. 
3. Execute the project exe file. 

Thanks!
