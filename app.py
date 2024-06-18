import os
import openai
from retry import retry
import re
from string import Template
import json
import ast
import time
import pandas as pd
from graphdatascience import GraphDataScience
import glob
from timeit import default_timer as timer
from dotenv import load_dotenv

load_dotenv()

def clean_text(text):
  clean = "\n".join([row for row in text.split("\n")])
  clean = re.sub(r'\(fig[^)]*\)', '', clean, flags=re.IGNORECASE)
  return clean


article_txt = """STRATEGIC REPORT

Group Chief Executive’s review

Alison Rose DBE
Group Chief Executive Officer

We agreed further measures for 2023 which include a one-off
£1,000 cost of living cash payment for c.42,000 colleagues in
the UK, Republic of Ireland and Channel Islands, and c.60,000
people globally. The 2023 pay proposal also includes a minimum
increase of £2,000 for almost all of the colleagues covered by it.
Taken together, this will mean that c.80% of lower-paid
colleagues covered by our negotiated pay approach will receive
an increase, plus a cash payment, equivalent to 10% or more of
their fixed pay. In the UK, our rates of pay continue to exceed
the ‘Living Wage Foundation’ benchmarks and, for our major
hubs outside the UK, we continue to pay above the minimum
and living wage rates in the Republic of Ireland as well as
exceeding the minimum wage benchmarks in India and Poland.

In light of these challenging economic circumstances, we
focused on putting in place proactive support to help people,
families and businesses to manage, and to help alleviate the
financial pressures being felt by those who were most vulnerable.
The strength of our balance sheet has allowed us to stand
alongside our customers and help them to navigate this
heightened uncertainty, as well as delivering a strong financial
performance for NatWest Group and value for shareholders.

Support for the cost of living
We responded quickly and meaningfully, proactively contacting
our customers to offer support and information on the cost of
living. In addition, we carried out c.0.7 million financial health
checks in 2022 and launched our credit score feature in our
mobile app to help customers understand their credit score. Our
online cost of living hub was also established to share resources
and tools, informing customers of the support that is available to
them, as well as support through third parties. These measures
were in addition to £4 million in donations to provide grants and
support, delivered in collaboration with organisations including
Citizens Advice, The Trussell Trust, Step Change and PayPlan.
As one of the leading banking partners of UK business, we
have taken a range of actions on charges, waiving fees on
some products where appropriate, including freezing standard
published tariffs on Business Current Accounts for 12 months
to help SMEs, and offering free card machine hire for new
customers on our payment service Tyl.

New and emerging social, commercial and economic
trends are shaping our customers’ financial lives and there are
important opportunities to transform our relevance and value to
customers, building on their trust. We will do this by delivering
personalised solutions throughout customers’ lifecycles;
embedding our services in our customers’ digital lives;
and supporting customers’ sustainability transitions.
FINANCIAL STATEMENTS

Championing the potential of UK
businesses is about more than just providing
financial backing.

RISK AND CAPITAL MANAGEMENT

Building strong
relationships
to help businesses
thrive

Watch the
story online
The QR code above directs to a case study video on our 2022 Annual Report webpage.
None of the information on that webpage (including the case study video) is, or should be
read as being, incorporated by reference into this report.

NatWest Group | 2022 Annual Report and Accounts

15


STRATEGIC REPORT

Market environment

Adapting to evolving
market trends

Economy
Overview

Our response

Customers
Overview

NatWest Group | 2022 Annual Report and Accounts

Cyberattacks pose a constant risk to our operations, both in
relation to our own digital estate and indirectly with regard
to our supply chain. Cybercrime continues to evolve rapidly.
Attacks may be from individuals or highly organised criminal
groups intent on stealing money or sensitive data, or potentially
holding organisations to ransom.
Our response
We continue to invest significant resources in the development
and evolution of cybersecurity controls, to deploy rigorous due
diligence with regard to third parties and to work to protect
and educate our colleagues and customers on fraud and scam
activity. To provide continuity of service for customers with
minimal disruption, we monitor and assess a diverse and
evolving array of threats, both external and internal, as well
as developing, strengthening or adapting existing control
capability to be able to absorb and adapt to such disruptions.

Technology

Climate change

Overview

Overview

New business models and customer behaviours continue
to evolve rapidly through advancing technology alongside
large-scale societal changes. In the post-pandemic era, we
recognise the growing role of technology in everything from
digital work environments to the access and delivery of goods
and services, including those within the financial sector.

Climate change represents an inherent risk to NatWest Group,
not only from its impact on the global economy, our customers,
suppliers and counterparties, but also through its potential
effects on asset values, operational costs and business models
as the essential transition to a net-zero economy accelerates.
These risks are subject to increasing regulatory, legislative,
political and societal change. Conversely, the requirement to
reduce carbon emissions also means NatWest Group has a
significant role to play in areas such as the provision of
climate and sustainable funding and financing.

We have remained
focused on removing
barriers to doing business
and providing more
opportunities for
companies to grow.

Geographical split of
climate and sustainable
funding and financing
in 2022(1)

£1.2bn

£12.3bn

Total
£24.5bn

£11.0bn

United Kingdom: £12.3bn
Western Europe: £11.0bn
Other: £1.2bn

(1) Since 1 July 2021, UK £17.8 billion, Western Europe £13.0 billion and Other
£1.8 billion. Geography for band issuance is linked to the region of the issuer;
for loans it is linked to the region of operation of the borrowing customer.
(*) Within the scope of EY assurance. Refer to page 70.

Regulation
Overview
We operate in a highly regulated market which continues
to evolve in scope. Areas of current regulatory focus include:
delivering good customer outcomes, in particular the Financial
Conduct Authority’s (FCA) new requirements for a Consumer
Duty, which expands its rules and principles to force firms to
provide better consumer protection; operational resilience,
in light of the UK authorities’ policy requirements; climate
change, and the development of the regulatory framework
for sustainable finance; fraud and financial crime, with a focus
on protecting customers from ever more sophisticated scams;
capital and liquidity management, including the UK’s approach
to the implementation of Basel III; the UK’s future regulatory
framework, following its exit from the European Union and
the opportunities that this provides; digital currencies, with
the development of both public (central bank digital currencies)
and private (e.g. stablecoins) offerings which have the potential
to materially change the digital payments landscape; improving
diversity, equity and inclusion in financial services through
policy developments focused on improved data collection
and reporting, and use of targets for representation.
Our response
We constantly monitor regulatory change and work with our
regulators to help shape those developments that materially
impact the bank, lobbying when necessary either bilaterally
or in partnership with one of our affiliated industry bodies.
We implement new regulatory requirements where applicable
and use our frequent engagement meetings with regulators
to discuss key regulatory priorities.

NatWest Group | 2022 Annual Report and Accounts

ADDITIONAL INFORMATION

16

Overview

FINANCIAL STATEMENTS

Expectations of banks have shifted markedly in recent years.
Customers are wanting banks to deliver a better service:
one that is simpler, more relevant and more purposeful.
How customers access our products and services has already
changed with increasing numbers of customers reaching us
online and through our mobile app. The ways people live, work
and run businesses are also altering at pace, with the pandemic
accelerating the trend towards more digital services, while also
seeing a proliferation of ‘side-hustle’ businesses. As well as
monitoring these longer-term trends we have also been
extremely mindful of the impact of rising prices during 2022
and the potential financial distress that this could cause the
customers, businesses and communities we serve.

Cyber threats

RISK AND CAPITAL MANAGEMENT

We know the tough economic conditions many of our customers
have faced throughout 2022. As such, we have remained
focused on removing barriers to doing business and providing
more opportunities for companies to grow, helping the economy
to build back better through initiatives such as our Accelerator
programme, our national and regional SME Taskforce boards
and our Business Builder toolkit, as well as supporting young
enterprise through our involvement with The Prince’s Trust.

In response to the continued increases in the cost of living
across the UK, we have put in place a range of targeted
measures to support those who are likely to need it most,
including proactive contacts to our customers to offer support
and information. In addition, we carried out c.0.7 million financial
health checks in 2022 and launched our credit score feature in
our mobile app to help customers understand their credit score.
Our online cost of living hub was also established to share
resources and tools, informing customers of the support that
is available to them, as well as support through third parties.
These measures were in addition to £4 million in donations
to provide grants and support, delivered in collaboration with
organisations including Citizens Advice, The Trussell Trust,
Step Change and PayPlan. Meanwhile, as we look ahead to the
next phase of our strategy, our future growth will be based on
building new forms of relevance and trust with our customers,
as well as supporting them through the challenges of today. We
have identified three areas for sustainable future growth where
we are well placed to do this: delivering personalised solutions
throughout our customers’ lifecycles; embedding our services
in our customers’ digital lives; and supporting our customers’
sustainability transitions.

As part of the implementation of its climate ambitions, at
NatWest Group’s AGM in April 2022, ordinary shareholders
passed an advisory ‘Say on Climate’ resolution. Through the
bank’s first climate resolution, the Board asked shareholders to
support our strategic direction on climate change, our intention
to develop a Climate transition plan and for annual progress
reports to be published. 92.58% of votes cast were in favour of
the resolution, indicating strong support for our climate strategy.
We also became the first UK bank, and one of the largest banks
globally to date, to have science-based targets validated by
the Science Based Targets initiative (SBTi). These targets,
which cover 79% of our lending activities by exposure as at
31 December 2019, underpin the initial iteration of our Climate
transition plan, which is incorporated within our 2022 Climaterelated Disclosures Report. We provided £24.5 billion(*) climate
and sustainable funding and financing in 2022, bringing
the cumulative contribution towards our target to provide
£100 billion between 1 July 2021 and the end of 2025, to
£32.6 billion. As at the end of 2022, we had reduced our direct
own operations emissions by 46%, against a 2019 baseline, with
a plan to achieve a 50% reduction by 2025. Achievement of our
climate ambitions is dependent on timely UK Government policy
and technology developments, as well as on our customers
and society to respond. At the same time, as a purpose-led
organisation, we aim to engage and support our customers’
transition to a net-zero economy. Read more in the 2022
Climate-related Disclosures Report.

GOVERNANCE

In 2022, the UK economy continued its recovery from the
impact of COVID-19 and lockdown restrictions, with GDP
approaching pre-pandemic levels. Russia’s invasion of Ukraine
and other global factors led to very large increases in energy
costs and other commodities during the year. The resulting
high inflation prompted central banks to tighten monetary policy
and markets to anticipate significant increases in interest rates,
leading to asset market volatility. In the UK the government
announced a significant easing of fiscal policy, with measures
to protect households from some of the increase in energy
prices, as well as support for businesses and a reversal of some
planned tax rises. Other countries introduced similar measures
through a variety of policies. Sterling fell against the US dollar
and the euro. In the longer term, demographic change, climate
change, high levels of debt and inequality could all have financial
impacts for our customers.

Our response

Our response

We are leveraging technology to deliver value through the
lifecycles of our customers. By helping them more and in
technologically-embedded ways, our relationships should
become closer and deeper, as well as more valuable. We
continue to develop new services, based on an understanding of
customers’ lives, that more closely fit with what our customers
want. Whether this is through new commercial offers that help
run invoice management and cash flow analysis, integrated
payments solutions or AI-based customer service, each of
these innovations is designed to benefit customers, society
and the economy, as well as being a driver of long-term
sustainable value.

"""

openai.api_key = os.getenv('OPENAI_API_KEY')

# GPT-4 Prompt to complete
@retry(tries=2, delay=5)
def process_gpt(system,
                prompt):

    completion = openai.chat.completions.create(
        # engine="gpt-3.5-turbo",
        model="gpt-4",
        max_tokens=2500,
        # Try to be as deterministic as possible
        temperature=0,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]
    )
    nlp_results = completion.choices[0].message.content
    return nlp_results

prompt1="""From the Annual Report text below, extract the following Entities & relationships described in the mentioned format
0. ALWAYS FINISH THE OUTPUT. Never send partial responses
1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. Document must be summarized and stored inside Case entity under `summary` property. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Paper',id:string,summary:string //Title of the article;`id` property is the title of the paper, in lowercase & camel-case & should always start with an alphabet
    label:'Company',id:string,name:string //Name of organisation;`id` property is the name of the company, in lowercase & camel-case & should always start with an alphabet
    label:'Person',id:string,name:string //Person mentioned in the text;`id` property is the name of a person, in lowercase & camel-case & should always start with an alphabet;
    label:'BusinessTrend',id:string,name:string //any known business term within the text,summary:string //Summary of the trend as defined by openAI;`id` property is the name of the business trend, in lowercase & camel-case & should always start with an alphabet
    label:'TechnologyTrend' id:string,name:string //any known technology term within the text,summary:string //Summary of the trend as defined by openAI;`id` property is the name of the technology trend, in lowercase & camel-case & should always start with an alphabet
    label:'Risk' id:string,name:string //any known factor which might present a risk to the organisation, summary:string //Summary of the trend as defined by openAI;`id` property is the name of the risk, in lowercase & camel-case & should always start with an alphabet
    label:'MA' id:string,name:string //any known mergers or acquisitions completed or planned, summary:string //Summary of the merger or acquisitions as defined by openAI;`id` property is the name of the merger or acquisitions, in lowercase & camel-case & should always start with an alphabet
    label:'ExternalFactor' id:string,name:string //any known external factors which might influcence or impact the organisation, summary:string //Summary of the trend as defined by openAI;`id` property is the name of the external factor, in lowercase & camel-case & should always start with an alphabet
    label:'Legal'id:string,name:string //any known legal issues which might impact the organisation, summary:string //Summary of the trend as defined by openAI;`id` property is the name of the legal issue, in lowercase & camel-case & should always start with an alphabet

3. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. You will have to generate as many relationships as needed as defined below:
    Relationship types:
    paper|MENTIONS_PERSON|person
    paper|MENTIONS_COMPANY|company
    company|MENTIONS_COMPANY|person
    paper|MENTIONS_BUSINESSTREND|businesstrend
    paper|MENTIONS_TECHNOLOGYTREND|technologytrend
    paper|MENTIONS_RISK|risk
    paper|MENTIONS_MERGER|ma
    paper|MENTIONS_EXTERNALFACTOR|externalfactor
    paper|MENTIONS_LEGAL|legal
    person|ASSOICATED_TO|externalfactor
    person|ASSOICATED_TO|ma
    person|ASSOICATED_TO|risk
    person|ASSOICATED_TO|businesstrend
    person|ASSOICATED_TO|technologytrend


The output should look like :
{
    "entities": [{"label":"Paper","id":string,"summary":string}],
    "relationships": ["paper|MENTIONS_PERSON|businesstrend"]
}

Case Sheet:
$ctext
"""

def run_completion(prompt, results, ctext):
    try:
      system = "You are a helpful business analyst who extracts relevant information and store them on a Neo4j Knowledge Graph"
      pr = Template(prompt).substitute(ctext=ctext)
      res = process_gpt(system, pr)
      results.append(json.loads(res.replace("\'", "'")))
      return results
    except Exception as e:
        print(e)

prompts = [prompt1]
results = []
for p in prompts:
  results = run_completion(p, results, clean_text(article_txt))

#print(results)

#pre-processing results for uploading into Neo4j - helper function:
def get_prop_str(prop_dict, _id):
    s = []
    for key, val in prop_dict.items():
      if key != 'label' and key != 'id':
         s.append(_id+"."+key+' = "'+str(val).replace('\"', '"').replace('"', '\"')+'"')
    return ' ON CREATE SET ' + ','.join(s)

def get_cypher_compliant_var(_id):
    return "_"+ re.sub(r'[\W_]', '', _id)

def generate_cypher(in_json):
    e_map = {}
    e_stmt = []
    r_stmt = []
    e_stmt_tpl = Template("($id:$label{id:'$key'})")
    r_stmt_tpl = Template("""
      MATCH $src
      MATCH $tgt
      MERGE ($src_id)-[:$rel]->($tgt_id)
    """)
    for obj in in_json:
      for j in obj['entities']:
          props = ''
          label = j['label']
          id = j['id']
          if label == 'Case':
                id = 'c'+str(time.time_ns())
          elif label == 'Person':
                id = 'p'+str(time.time_ns())
          varname = get_cypher_compliant_var(j['id'])
          stmt = e_stmt_tpl.substitute(id=varname, label=label, key=id)
          e_map[varname] = stmt
          e_stmt.append('MERGE '+ stmt + get_prop_str(j, varname))

      for st in obj['relationships']:
          rels = st.split("|")
          src_id = get_cypher_compliant_var(rels[0].strip())
          rel = rels[1].strip()
          tgt_id = get_cypher_compliant_var(rels[2].strip())
          stmt = r_stmt_tpl.substitute(
              src_id=src_id, tgt_id=tgt_id, src=e_map[src_id], tgt=e_map[tgt_id], rel=rel)

          r_stmt.append(stmt)

    return e_stmt, r_stmt

ent_cyp, rel_cyp = generate_cypher(results)

print(ent_cyp)

connectionUrl = os.getenv('CONN_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

gds = GraphDataScience(connectionUrl, auth=(username, password))
gds.version()

gds.run_cypher('CREATE CONSTRAINT unique_paper_id IF NOT EXISTS FOR (n:Paper) REQUIRE n.id IS UNIQUE')
gds.run_cypher('CREATE CONSTRAINT unique_person_id IF NOT EXISTS FOR (n:Person) REQUIRE (n.id) IS UNIQUE')
gds.run_cypher('CREATE CONSTRAINT unique_company_id IF NOT EXISTS FOR (n:Company) REQUIRE (n.id) IS UNIQUE')
gds.run_cypher('CREATE CONSTRAINT unique_business_trend IF NOT EXISTS FOR (n:BusinessTrend) REQUIRE n.id IS UNIQUE')
gds.run_cypher('CREATE CONSTRAINT unique_technology_trend IF NOT EXISTS FOR (n:TechnologyTrend) REQUIRE n.id IS UNIQUE')

# Ingest the entities
for e in ent_cyp:
    gds.run_cypher(e)


# Ingest relationships now
for r in rel_cyp:
    gds.run_cypher(r)


def run_pipeline(count=191):
    txt_files = glob.glob("data/*.txt")[0:count]
    print(f"Running pipeline for {len(txt_files)} files")
    failed_files = process_pipeline(txt_files)
    print(failed_files)
    return failed_files

def process_pipeline(files):
    failed_files = []
    for f in files:
        try:
            with open(f, 'r') as file:
                print(f"  {f}: Reading File...")
                data = file.read().rstrip()
                text = clean_text(data)
                print(f"    {f}: Extracting E & R")
                results = extract_entities_relationships(f, text)
                print(f"    {f}: Generating Cypher")
                ent_cyp, rel_cyp = generate_cypher(results)
                print(f"    {f}: Ingesting Entities")
                for e in ent_cyp:
                    gds.run_cypher(e)
                print(f"    {f}: Ingesting Relationships")
                for r in rel_cyp:
                    gds.run_cypher(r)
                print(f"    {f}: Processing DONE")
        except Exception as e:
            print(f"    {f}: Processing Failed with exception {e}")
            failed_files.append(f)
    return failed_files

def extract_entities_relationships(f, text):
    start = timer()
    system = "You are a helpful Medical Case Sheet expert who extracts relevant information and store them on a Neo4j Knowledge Graph"
    prompts = [prompt1]
    all_cypher = ""
    results = []
    for p in prompts:
      p = Template(p).substitute(ctext=text)
      res = process_gpt(system, p)
      results.append(json.loads(res))
    end = timer()
    elapsed = (end-start)
    print(f"    {f}: E & R took {elapsed}secs")
    return results

failed_files = run_pipeline(200)

# If processing failed for some files due to API Rate limit or some other error, you can retry as below
failed_files = process_pipeline(failed_files)
print(failed_files)