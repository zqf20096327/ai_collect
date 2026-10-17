# RealPref Benchmark
This repository contains code and data for the paper **Towards Realistic Personalization: Evaluating Long-Horizon Preference Following in Personalized User-LLM Interactions**. It includes dataset and scripts for generation and evaluation.

## Overview
Beyond serving as general-purpose assistants that support users in everyday contexts, there is a growing need for LLMs to support personalized needs: As users engage in long-term interactions with LLMs, they naturally reveal personal information, such as preferences and habits, through various forms of expression. In turn, users expect assistants to adapt to such signals and provide tailored responses to serve individual needs.
<p align="center">
  <img src="figure/intro.png" alt="An Example of User-LLM Interaction" width="400">
</p>
<p align="center">
  <em>An Example of User-LLM Interaction: the conversation consists of several sessions on various topics. The user expresses a food preference in a previous session and then, after several sessions, asks the LLM for food-related recommendations.</em>
</p>

We aim to answer: Can LLMs effectively 
- **capture** user preferences from complex user expressions, 
- **retain and follow** user preferences across extended interaction contexts
- **generalize** user preference understanding to unseen scenarios? 

We propose ***RealPref***, a benchmark that features diverse user biographies, varying levels of preference expressions, and comprehensive evaluation protocols, constructing a testing environment that simulates the complexities of realistic, long-horizon user-LLM interactions. Key components and features are summarized below:

- **Dataset Construction**: a user-centered long-horizon dialogue dataset that incorporates diverse preference expressions (from explicit to implicit) and generalization scenarios to simulate the complexity of authentic user-LLM interactions.
- **Evaluation Framework**: a multi-faceted evaluation protocol consisting of multiple-choice, true-or-false, and open-ended tasks, supported by granular and systematic rubrics to assess open-ended answers.

<p align="center">
  <img src="figure/generation_pipeline.png" alt="Generation Pipeline Overview" width="700">
</p>
<p align="center">
  <em>Generation Pipeline Overview. Starting from user personas, we construct detailed user profiles and biographies with diverse preferences. Using these, we construct rich conversation sessions that cover preference expressions from explicit to implicit, and concatenate them into a long-horizon context for each user. For each preference, generation and classification task queries are designed, with corresponding evaluation protocols.</em>
</p>

## File Structure

```  
root/
├── data/
│   └── persona_hub.jsonl 	# PersonaHub dataset: the persona pool from which our seed personas are sampling from
│   └── selected_personas.json          # preliminary sampled personas
│
├── template/ 				# template for data generation
│   ├── conversation_template.json      # template for conversation generation
│   ├── cot_qa.json                     # few-shot chain-of-thought examples
│   ├── event_template.json             # template for events generation
│   ├── judge_score_template.json       # template for LLM-as-a-judge outputs
│   ├── preference_template.json        # template for preferences generation
│   ├── profile_template.json           # template for user profile generation
│   └── qa_template.json                # template for preference-query generation
│
└── test_data/				# generated test dataset
│   ├── user/				# user data folder
│   │   └── [uid]/                      # user-specific data of user with [uid]
│   │       ├──data_[uid]_profile.json              # user profile data: demographics, persona, biography, preferences
│   │       ├──data_[uid]_event_conversation.json   # user life-event conversation data
│   │       ├──data_[uid]_pref_conversation.json    # user preference_expression conversation data
│   │       ├──data_[uid]_qa.json                   # user preference-query for original preferences
│   │       └──data_[uid]_qa_infer.json             # user preference-query for generalized preferences
│   │
│   ├── context_history_index.json		# the index of conversation sessions for concatenating into a complete context history
│   ├── profiles.json					# extended user profile for all users in dataset
│   └── random_conversation.json		# random conversation data
│
├── prompts.py 	        # prompts for generation pipeline and LLM-as-a-judge
├── prepare_data.py 	# code for generation pipeline
├── test.py 	        # code for model testing
├── judge.py 	        # code for test result evaluation
├── utils.py 	        # tool function set
├── run_generation.sh   # bash script example for running prepare_data.py
├── run_test.sh         # bash script example for running test.py
├── run_judge.sh        # bash script example for running judge.py
├── readme.md
└── requirements.txt

```

## Benchmark Dataset

All the generated user data for testing are stored in ```test_data/```, 

### User Profile File

```user/{uid}/data_{uid}_profile``` stores all the core user information, including personas, demographics, life events, original preferences, preference initialize events, generalized preferences. The following details the data contents in this file.

#### Profile Data
Basic user profile with demographics and persona descriptions. Format:
``````
"Demographics": {
    "Name": "Emma Walsh",
    "Birth": "1991",
    "Gender": "Female",
    "Education": "Diploma in Makeup Artistry",
    "Occupation": "Makeup Artist",
    "Economic Status": "Middle Class",
    "Marital Status": "Single"
    },
"Original Persona": "xxx",  # sampled from PersonaHub
"Extended Persona": "xxx"   # extended during generation
``````
#### Life Event Data
User life event list, constructing personal biography. Format:
``````
"Events": [
        {
            "Date": "2009/09/01",
            "Event": "Enrolled in a professional makeup artistry diploma program at a local beauty academy, developing fundamental technical skills and industry knowledge.",
            "Duration": "years"
        },
        ...,
]
``````
#### Original Preference Data
User original preference designed based on basic profiles. Format:
``````
"Preference": [
        {
            "Type": "1",    # description type eg. type 1 means prefer something over another
            "Topic": "Education: Learning Resources",
            "Preference": "Prefers hands-on workshops and live demonstrations over online pre-recorded courses, as she finds direct interaction and immediate feedback helps her retain creative techniques better."
        },
        ...,
]
``````
#### Original Preference Initialize Event Data
User original preference is equipped with an initialize event idicating the user experience and how the user developed the preference. Format:
``````
"Pref_init": {
        "Pref_id": {
            "Preference": "Prefers hands-on workshops and live demonstrations over online pre-recorded courses, as she finds direct interaction and immediate feedback helps her retain creative techniques better.",
            "Type": "1",
            "Topic": "Education: Learning Resources",
            "Date": "2013/04/12",
            "Event": "Attended her first in-person makeup workshop where she received direct feedback from experts, realizing how much faster and more creatively she learned compared to previous online courses."
        },
        ...,
}
``````
#### Generalized Preference Data
User generalized preference that can be rationally inferred from original preference list. Format:
``````
"Pref_generalized": {
        "Pref_id": {
            "Infer_reason": "Her dislike of monotonous routines, regimented systems, and classic or mainstream offerings across various domains (food, beauty, exercise, music) suggests a desire for originality and novelty.",
            "Topic": "Entertainment: Movies & Shows",
            "Preference": "Dislikes formulaic blockbuster movies and prefers independent films or experimental cinema, as unconventional storytelling stimulates her creative thinking."
        },
        ...,
}
``````

### Conversation Files
We have three types of conversation sessions, with corresponding data files and formats listed below. 

#### Random Conversations
```random_conversation.json```: random conversation that contain no use profile data, can be used for all users. Format:
``````
"session_id": [ # conversation sessions, no timestamp for random conversation
    {
        "user": "I'm having trouble connecting to Wi-Fi on Windows 10. Any troubleshooting tips?",
        "assistant": "xxx
    },
    xxx,
]
``````

#### Life Event Conversations
```user/{uid}/data_{uid}_event_conversation.json```: general life event conversations that is organized by personal life stages, indicating user background, profiles in the conversation. Format:

``````
{
    "stage_id": {			# life event stage, correspondent to the event list intervals in user profile. 
                # eg. "0": stage before life event_0, "1": state between event_0 and event_1
        "session_id": [		# conversation sessions with timestamp
                {"timestamp": ,"user": ,"assistant": },
                {"timestamp": ,"user": ,"assistant": }
    ]
}
}
``````

#### Preference Expression Conversations
```user/{uid}/data_{uid}_pref_conversation.json```: user preference expression conversation that is organized by user preference index and preference expression type. Format:

``````
{
    "Pref_0": {			# preference id, same as in the user profile file
        "1": {			# preference expression type level, 1-4 from explicit to implicit
            "session_1": [		# conversation sessions with timestamp
                {"timestamp": ,"user": ,"assistant": },
                {"timestamp": ,"user": ,"assistant": }
            ]
        }
    }
}
``````
#### Context Index list
```context_history_index```: we designed context index list to concatenate the above 3 types of conversation sessions. The list is organized by context_config and user id. Format:
``````
{
    "context_config": { # context config controls the random conversation insertion in the history, and thus control context lengths.
        "uid": [
            "Event_0_session_1", # session index, indicating that the corresponding session conversation occurred here.
            "Random_session_251",
            "Event_1_session_2",
            "Random_session_734",
            "Pref_0",
            ...
        ]
    }
}
``````
The mapping of context config key to the context name in the paper is: 
``````
mix_0_0 -- simple context: no random conversation inserted, 2K token context in average
mix_5_0 -- normal context: 37K token context in average
mix_10_0 -- long context: 72K token context in average
mix_20_0 -- very long context: 142K token context in average
mix_5_15 -- extended context: 142K token context in average
mix_5_30 -- extreme context: 247K token context in average
``````

### Query and Answer Files

```user/{uid}/data_{uid}_qa.json``` stores the QA data for the user's original preferences. ```user/{uid}/data_{uid}_qa_infer.json``` stores the QA data for the user's generalized preferences. Format:

``````
{
	"Pref_id": { 		# reference id, same as in the user profile file
        "Preference": "xxx"	# preference to test
        "Query": "xxx"		# query, serve for both MCQ and open-ended question
        "MCQ_options": {"A": "xxx" ,"B": "xxx" ,"C": "xxx" ,"D": "xxx" }, # MCQ options
        "Correct_Answer": "xxx" 	# Correct option in MCQ
        "T_Query": "xxx" 		# True or False question, combine the query and the right option in MCQ.
        "F_Query": "xxx" 		# True or False question, combine the query and a wrong option in MCQ.
    }
}
``````

## Use the Benchmark
The following is an introduction of our codes for three phases: data generation, test, and evaluation judgement. Our code is for reference only. You can also create your own code files to freely use the datasets we provided.

Our code is generally working with API based LLM. If you also want to use API based LLM (e.g., openai api or openrouter), create an ```.env``` file and fill in your own API key (```OPENAI_API_KEY=xxxxxx```). The key will be used for intializing llm client in the first step. You can also create your own llm client to use your locally deployed LLMs.

### Generation Pipeline
- ```prepare_data.py``` stores all the code needed for each step in the generation pipeline, from user persona to conversations and QAs. Because the generation pipeline is relerively long incuding several steps, data can be generated selectively step by step in the main part.
- ```prompts.py``` stores the prompts of each step for data generation. 
- ```run_generation.sh``` provides a bash script to run ```prepare_data.py```. Example:
    ``````
    python ./prepare_data.py -s 26 -n 10 >> ./log/output.log 2>&1 
    # start generating user data from uid 26 to uid 35 (10 users), and output logs to file ./log/output.log.
    # by default, the data file will be created at ./test_data/user/{uid}/..., or you can also specify your own storage path
    ``````

### Test Pipeline
- ```test.py``` stores the code we used for testing API based LLMs, including build context, build test data, and query llm to get responses.
- ```run_test.sh``` provides a bash script to run ```test.py```. Example:
    ``````
    python ./test.py -t testmodelname -m zero_shot -c mix_5_0 -s 1 -n 100 -p 4 -q mcq tf >> ./log/test_output1.log
    # specify testmodelname as model version to be tested.
    # specify -m as test methods: [zero_shot, reminder, cot, rag].
    # specify -c as context config name.
    # specify -s and -n as starting uid and number of user data to be tested.
    # specify -p as preference expression type to be tested.
    # specify -q as question task type: [mcq, tf, open]
    # by default, the response data file storing the responses gathered from llms will be created at ./{testmodelname}_{method}_{config}_{qtype}.json, or you can also specify your own storage path
    ``````


### Judge Pipeline
- ```judge.py``` stores the code we used for judging the response gathered from llms, including classification accuracy calculation, LLM-as-a-Judge for open-ended answer with average score calculation.
- ```prompts.py``` stores the detailed evaluation rubrics we used for conducting LLM-as-a-Judge.
- ```run_judge.sh``` provides a bash script to run ```judge.py```. Example:
    ``````
    python ./judge.py -m judge_model -f answer_file -t open >> ./log/judge_output1.log
    # specify judge_model llm judge.
    # specify answer_file as the gathered response file from test llms (generated from running test.py)
    # specify -t as the task type needed to be judged: [mcq, tf, open]
    # by default, the judge result will add to the answer_file and calculate average scores.
    ``````