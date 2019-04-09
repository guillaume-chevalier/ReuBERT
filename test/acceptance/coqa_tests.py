from src.infrastructure.pipeline_steps.bert_model_wrapper import BertModelWrapper
from src.infrastructure.pipeline_steps.bert_natural_answer_postprocessor import BertNaturalAnswerPostprocessor
from src.util.ResponseEvaluator import ResponseEvaluator

import os
import json
user_input = [
    "William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright and actor, widely regarded ",
    "as the greatest writer in the English language and the world's greatest dramatist.[2][3][4] He is often called England's national poet and "
    "the \"Bard of Avon\".[5][b] His extant works, including collaborations, consist of approximately 39 plays,[c] 154 sonnets, two long narrative poems, "
    "and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than "
    "those of any other playwright.[7] Shakespeare was born and raised in Stratford-upon-Avon, Warwickshire. At the age of 18, he married Anne Hathaway, with "
    "whom he had three children: Susanna and twins Hamnet and Judith. Sometime between 1585 and 1592, he began a successful career in London as an actor, writer, "
    "and part-owner of a playing company called the Lord Chamberlain's Men, later known as the King's Men. At age 49 (around 1613), he appears to have retired to"
    " Stratford, where he died three years later. Few records of Shakespeare's private life survive; this has stimulated considerable speculation about such matters "
    "as his physical appearance, his sexuality, his religious beliefs, and whether the works attributed to him were written by others.[8][9][10] Such theories are "
    "often criticised for failing to adequately note that few records survive of most commoners of the period. Shakespeare produced most of his known works between "
    "1589 and 1613.[11][12][d] His early plays were primarily comedies and histories and are regarded as some of the best work produced in these genres. Until about "
    "1608, he wrote mainly tragedies, among them Hamlet, Othello, King Lear, and Macbeth, all considered to be among the finest works in the English language.[2][3][4] "
    "In the last phase of his life, he wrote tragicomedies (also known as romances) and collaborated with other playwrights. Many of Shakespeare's plays were published "
    "in editions of varying quality and accuracy in his lifetime. However, in 1623, two fellow actors and friends of Shakespeare's, John Heminges and Henry Condell, "
    "published a more definitive text known as the First Folio, a posthumous collected edition of Shakespeare's dramatic works that included all but two of his plays."
    "[13] The volume was prefaced with a poem by Ben Jonson, in which Jonson presciently hails Shakespeare in a now-famous quote as \"not of an age, but for all time\".[13]"
    "Throughout the 20th and 21st centuries, Shakespeare's works have been continually adapted and rediscovered by new movements in scholarship and performance. His plays remain "
    "popular and are studied, performed, and reinterpreted through various cultural and political contexts around the world."]

question = "Where was Shakespeare raised?"

def extract_question_from_coqa():
    with open(os.path.join(__file__, '../coqa-dev-v1.0.json'), encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


bert_wrapper = BertModelWrapper()
best_post_processor = BertNaturalAnswerPostprocessor()
bert_evaluator = ResponseEvaluator()

def test_bert_postprocessor():
    story = "Once upon a time, in a barn near a farm house, there lived a little white kitten named Cotton." \
            " Cotton lived high up in a nice warm place above the barn where all of the farmer's horses slept. " \
            "But Cotton wasn't alone in her little home above the barn, oh no. She shared her hay bed with her mommy " \
            "and 5 other sisters. All of her sisters were cute and fluffy, like Cotton. But she was the only white one " \
            "in the bunch. The rest of her sisters were all orange with beautiful white tiger stripes like Cotton's" \
            " mommy. Being different made Cotton quite sad. She often wished she looked like the rest of her family. " \
            "So one day, when Cotton found a can of the old farmer's orange paint, she used it to paint herself like " \
            "them. When her mommy and sisters found her they started laughing. \"What are you doing, Cotton?!\" \"I only wanted to be more like you\"." \
            "Cotton's mommy rubbed her face on Cotton's and said \"Oh Cotton, but your fur is so pretty and special, " \
            "like you. We would never want you to be any other way. And with that, Cotton's mommy picked her " \
            "up and dropped her into a big bucket of water. When Cotton came out she was herself again. Her " \
            "sisters licked her face until Cotton's fur was all all dry. \"Don't ever do that again, Cotton!\" they " \
            "all cried. \"Next time you might mess up that pretty white fur of yours and we wouldn't want that! " \
            "Then Cotton thought, \"I change my mind. I like being special\"."
    question = "Did she live alone?"
    bert_res = [(0.38090299723492976, "Cotton wasn't alone in her little home above the barn, oh no"), (0.26082781056632415, "Cotton wasn't alone"), (0.07662491659353675, "But Cotton wasn't alone in her little home above the barn, oh no"), (0.0662266001610968, "Cotton wasn't alone in her little home above the barn, oh no."), (0.05246981350895664, "But Cotton wasn't alone"), (0.027339701347176133, "Cotton wasn't alone in her little home above the barn, oh no. She shared her hay bed with her mommy and 5 other sisters."), (0.016248778451646014, "Cotton wasn't alone in her little home above the barn"), (0.01582834090282384, "Cotton wasn't alone in her little home above the barn, oh no. She shared her hay bed with her mommy and 5 other sisters"), (0.014138185568693588, "Cotton wasn't alone in her little home above the barn,"), (0.013322572283377652, "But Cotton wasn't alone in her little home above the barn, oh no."), (0.01330056290201684, "wasn't alone in her little home above the barn, oh no"), (0.012172311463110286, 't alone in her little home above the barn, oh no'), (0.011121160451637777, "Cotton wasn't"), (0.0091077169941329, "wasn't alone"), (0.008335133541877211, 't alone'), (0.005787933137609206, 'oh no'), (0.005499831586065209, "But Cotton wasn't alone in her little home above the barn, oh no. She shared her hay bed with her mommy and 5 other sisters."), (0.004292706112305063, "Cotton wasn't alone in her little home"), (0.0032687096259216776, "But Cotton wasn't alone in her little home above the barn"), (0.0031841316825997443, "But Cotton wasn't alone in her little home above the barn, oh no. She shared her hay bed with her mommy and 5 other sisters"), (8.58841627496776e-08, '')]

    output = (story, question, bert_res)

    transformed_answer = best_post_processor.transform_one(output)
    print(transformed_answer)

def test_bert_with_coqa():
    total_qu = 0
    good_res = 0
    data = extract_question_from_coqa()
    for elem in data['data']:
        story = elem['story']

        for q_index in range(len(elem['questions'])):
            total_qu += 1
            question = elem['questions'][q_index]['input_text']
            answer = elem['answers'][q_index]['input_text']

            output = bert_wrapper.transform_one(([story], question))

            transformed_answer = best_post_processor.transform_one(output)

            best_bert_ans = output[2][0][1]

            if bert_evaluator.is_response_close_enough_using_leveinstein(best_bert_ans, answer):
                good_res+=1


            print("number :", q_index)
            # print("story :", story)
            print("Question:", question)
            print("possible answer:", answer)
            print("bert answer:", output[2])
            print("transformed answer:", transformed_answer)
            print("accuracy :", good_res/total_qu)

test_bert_with_coqa()
# test_bert_postprocessor()


