# Graph-Implementation-for-Vaccine-Problem-Statement
Problem Statement 
Since the advent of different viral strains, governments across the world are researching combining 
available vaccines to enhance immunity. Vaccines can be deployed after a gap of a few months to 
battle various strains. Assume that you are a global COVID vaccine researcher and you want to map 
which vaccines have been found effective against a virus strain (either in the past or present). For this 
you need to have some system of storing these vaccines and the strains they have neutralized.
Assume that you have a list of N strains and M vaccines. For the sake of this assignment, let us 
assume that a particular vaccine could neutralize only two strains at max.
This is to write an application that maps COVID Strains and Vaccines and can answer the below queries:
1. List the unique strains and vaccines the researcher has collected in the system.
2. For a particular strain, help the reporter recollect the vaccines it has been neutralized by.
3. For a particular vaccine, list the strains that have been neutralized with it (past or present).
4. Identify if two vaccines neutralize similar strains. Vaccine A and vaccine B are considered to 
neutralize similar strains if they have been associated with the same strains (not necessarily at the 
same time or in the same year) 
5. Can two vaccines A and B be connected such that there exists another vaccine C where A and C 
are neutralizing similar strains and C and B are neutralizing similar strains. 
Requirements
1. Model the following problem as Graph based problem using Python 3.7. Clearly state how the 
vertices and edges can be modelled such that this graph can be used to answer the following 
queries efficiently.
2. Read the input from a file inputPS16.txt
3. You will output your answers to a file outputPS16.txt
4. Perform an analysis for the features above and give the running time in terms of input size: n
