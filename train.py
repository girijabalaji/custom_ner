#pip install spacy
#python -m spacy download en_core_web_sm


# ------------------------------------------------------#
# import spacy 

# nlp = spacy.load("en_core_web_sm")
# print(nlp.pipe_names)


# sentence = "Daniil Medvedev and Novak Djokovic have built an intriguing rivalry since the Australian Open decider, which the Serb won comprehensively."
# doc = nlp(sentence)
# print([(X, X.ent_iob_, X.ent_type_) for X in doc if X.ent_type_])

#------------------------------------------------- #

import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
trainData = [
    ("We are looking for a Full-stack Developer who is motivated to combine the art of design with the art of programming.", {"entities": [(21, 40, "JOB_ROLE")]}),
    ("As a Full stack Developer, you will develop applications in a very passionate environment being responsible for Front-end and Back-end development.", {"entities": [(5, 25, "JOB_ROLE")]}),
    ("Ivy Mobility is looking for Full-stack Dot net Tech Lead who has the ability to work in a fast-paced environment, on multiple projects concurrently.", {"entities": [(28, 56, "JOB_ROLE")]}),
    ("Previous experience working as a React.js Developer.", {"entities": [(33, 51, "JOB_ROLE")]}),
    ("Yellow Riddle is looking for a front-end Shopify Developer to join our growing team with our increasing volume of Shopify work.", {"entities": [(31, 58, "JOB_ROLE")]}),
    ("Experience working as a React Native Developer.", {"entities": [(23, 47, "JOB_ROLE")]}),
    ("Job Title: Lead / Senior React Native developer", {"entities": [(10, 47, "JOB_ROLE")]}),
    ("Job Title: Salesforce Developer (LWC)", {"entities": [(11, 31, "JOB_ROLE")]}),
    ("I'm hiring Python Developers - Tech Lead for Thryve Digital Health LLP\n\nOffice Location: Ramanujan IT City, Chennai\nTime Zone: General shift\nExperience: 8 to 12 years\nSkill Sets:\n1) Expertise in Python development.\n2) Good to have team leading skills.\n3) Good verbal and written communication skills.\n\nInterested candidates, kindly share your updated resume to prithiv.muralibabu@thryvedigital.com. Referrals are invited!",{"entities":[(11,40,"JOB_ROLE"),(45,70,"ORG"),(88,106,"ADDRESS"),(108,115,"LOCATION"),(126,143,"SHIFT_TYPE"),(152,170,"EXP"),(193,202,"SKILL"),(228,244,"SKILL"),(275,293,"SKILL"),(360,397,"EMAIL_ADDR")]}),
    ("Hello All,Greetings From #RiteSoftware #greatplacetowork #productbased #productdevelopment #Oracle We are #hiring #javafullstackdeveloper Exp: 5-10 Years Notice Period: Immediate Location : Bangalore (Work from Home is fine)Job Description:Java, Spring, Springboot, AngularJS/2+, Database 4-8 years’ Experience with Java/Spring and Angular development. Experience with Microservices development with Spring and Spring boot Experience with UI development with Angular and NodeJS Experience with DB technology for PostgreSQL and Oracle. Experience with Jenkins and DevOps tooling Experience with Azure Cloud preferred.",{"entities":[(26,38,"ORG"),(92,98,"SKILL"),(115,137,"JOB_ROLE"),(143,153,"EXP"),(190,199,"LOCATION"),(240,244,"SKILL"),(246,252,"SKILL"),(254,264,"SKILL"),(266,278,"SKILL"),(289,298,"EXP"),(316,320,"SKILL"),(321,327,"SKILL"),(332,339,"SKILL"),(471,477,"SKILL"),(512,522,"SKILL"),(527,533,"SKILL"),(551,558,"SKILL"),(594,599,"SKILL")]}),
    ("Hiring for HCL, Bangalore  Job Description We are looking for a professional Embedded Software Engineer to execute complete embedded software development lifecycle. The goal is to create scalable and optimized software systems.  Responsibilities - Design and implement Application software for embedded devices and systems from requirements to production and deployment. - Design, develop, code, test and debug Application software - Review code and design - Analyze and enhance efficiency, stability and scalability of system resources - Provide post production support  Requirements - Solid programming experience in C on Linux OS. - Experience in socket programming and multi-threading firmware development. - Experience in hands-on development and troubleshooting on embedded targets - Familiarity with software configuration management tools, defect tracking tools, and peer review  Good to have - Excellent understanding of IPC mechanisms such as Message queues, shared memory. - Experience in working with PostgreSQL. Writing optimized queries based off multiple tables. - Added advantages if worked on C++ STLs like Vectors, Maps etc.",{"entities":[(11,14,"ORG"),(16,25,"LOCATION"),(77,103,"JOB_ROLE"),(619,620,"SKILL"),(624,632,"SKILL"),(650,656,"SKILL"),(673,697,"SKILL"),(1013,1023,"SKILL"),(1110,1113,"SKILL")]}),
        ("Hiring for HCL, Bangalore  Akar Inti Enterprise is urgently hiring for Junior Software Engineer (Developer)  General Requirement : -Bachelor degree from IT or related major -Must have work experience for 2-3 as Software Engineer or Software Developer -Have knowledge about financial/core banking system or integration system -Fast learner, high logical thinking and able to work under pressure -Good in English  Must have this IT skill stacks : -System Architecture : Microservices -Programming Language : JAVA -Framework : Spring Boot, Struts, Hibernate, etc -Message Queue : Kafka -Database : PostgreSQL -Cache : Redis -Monitoring Tools : ELK, Prometheus, Kibana, Grafana, other Monitoring Tools -Container Management : Docker and Kubernetes -API Management : Istio, REST API, RESTFUL API -Devops Tools : ArgoCd, Gitlab CI/CD, Cloud CI/CD, Jenkins -Cloud technology: Huawei, GCP, AWS, etc  Work type : Hybrid Location : Kuningan, Jakarta Selatan preferable anyone who can join immediately  send CV to : afifah@aienterprise.id with subject email : Junior Developer",{"entities":[(11,14,"ORG"),(16,25,"LOCATION"),(27,47,"ORG"),(71,95,"JOB_ROLE"),(204,207,"EXP"),(232,250,"JOB_ROLE"),(211,228,"JOB_ROLE"),(403,410,"SKILL"),(506,510,"SKILL"),(524,535,"SKILL"),(537,543,"SKILL"),(545,554,"SKILL"),(577,582,"SKILL"),(595,605,"SKILL"),(615,620,"SKILL"),(658,664,"SKILL"),(666,673,"SKILL"),(722,728,"SKILL"),(733,743,"SKILL"),(762,767,"SKILL"),(807,813,"SKILL"),(792,798,"SKILL"),(815,827,"SKILL"),(829,840,"SKILL"),(842,849,"SKILL"),(869,875,"SKILL"),(904,910,"SHIFT_TYPE"),(922,930,"LOCATION"),(932,947,"LOCATION"),(1005,1027,"EMAIL_ADDR"),(1049,1065,"JOB_ROLE")]}),
]

nlp = spacy.blank("en") # load a new spacy model
db = DocBin() # create a DocBin object
for text, annot in tqdm(trainData): #data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        print(span)
        if span is None:
            print("Skipping entity")
        else:
        	ents.append(span)
    try:
        doc.ents = ents # label the text with the ents
        db.add(doc)
    except:
        print(text, annot)
db.to_disk("./traindata.spacy") # save the docbin object






