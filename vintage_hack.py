__author__ = 'MLadbrook'

import numpy as np
import random
import flask
app = flask.Flask(__name__)


words_four = ['help', 'dogs', 'cats', 'does', 'baby', 'burn', 'most', 'wake',
              'want', 'good', 'ball', 'case', 'camp', 'cost', 'deep', 'drug',
              'edge', 'five', 'fund', 'goal', 'hair', 'hire', 'item', 'kept',
              'lock', 'meal', 'mile', 'name', 'navy', 'play', 'sand', 'soul',
              'tiny', 'upon', 'wave', 'whom', 'zone', 'zero', 'yard', 'wish']
words_five = ['pleat', 'hello', 'tears', 'mouse', 'about', 'agree', 'alive',
              'arena', 'badly', 'beach', 'basis', 'booth', 'brief', 'catch',
              'chest', 'claim', 'civil', 'death', 'drink', 'earth', 'faith',
              'fifty', 'focus', 'frank', 'glass', 'guest', 'guide', 'horse',
              'human', 'index', 'issue', 'judge', 'known', 'laser', 'level',
              'light', 'loose', 'march', 'minus', 'motor', 'never', 'nurse',
              'ocean', 'ought', 'paper', 'photo', 'power', 'proud', 'queen',
              'ratio', 'rival', 'royal', 'score', 'shock', 'shoot', 'skill',
              'space', 'sport', 'steam', 'style', 'sugar', 'taste', 'title',
              'tough', 'truly', 'unity', 'virus', 'watch', 'worry', 'youth']
words_six = ['abroad','accept','access','across','acting','action','active',
             'actual','advice','advise','affect','afford','afraid','agency',
             'agenda','almost','always','amount','animal','annual','answer',
             'anyone','anyway','appeal','appear','around','arrive','artist',
             'aspect','assess','assist','assume','attack','attend','august',
             'author','avenue','backed','barely','battle','beauty','became',
             'become','before','behalf','behind','belief','belong','berlin',
             'better','beyond','bishop','border','bottle','bottom','bought',
             'branch','breath','bridge','bright','broken','budget','burden',
             'bureau','button','camera','cancer','cannot','carbon','career',
             'castle','casual','caught','center','centre','chance','change',
             'charge','choice','choose','chosen','church','circle','client',
             'closed','closer','coffee','column','combat','coming','common',
             'comply','copper','corner','costly','county','couple','course',
             'covers','create','credit','crisis','custom','damage','danger',
             'dealer','debate','decade','decide','defeat','defend','define',
             'degree','demand','depend','deputy','desert','design','desire',
             'detail','detect','device','differ','dinner','direct','doctor',
             'dollar','domain','double','driven','driver','during','easily',
             'eating','editor','effect','effort','eighth','either','eleven',
             'emerge','empire','employ','enable','ending','energy','engage',
             'engine','enough','ensure','entire','entity','equity','escape',
             'estate','ethnic','exceed','except','excess','expand','expect',
             'expert','export','extend','extent','fabric','facing','factor',
             'failed','fairly','fallen','family','famous','father','fellow',
             'female','figure','filing','finger','finish','fiscal','flight',
             'flying','follow','forced','forest','forget','formal','format',
             'former','foster','fought','fourth','french','friend','future',
             'garden','gather','gender','german','global','golden','ground',
             'growth','guilty','handed','handle','happen','hardly','headed',
             'health','height','hidden','holder','honest','impact','import',
             'income','indeed','injury','inside','intend','intent','invest',
             'island','itself','jersey','joseph','junior','killed','labour',
             'latest','latter','launch','lawyer','leader','league','leaves',
             'legacy','length','lesson','letter','lights','likely','linked',
             'liquid','listen','little','living','losing','lucent','luxury',
             'mainly','making','manage','manner','manual','margin','marine',
             'marked','market','martin','master','matter','mature','medium',
             'member','memory','mental','merely','merger','method','middle',
             'miller','mining','minute','mirror','mobile','modern','modest',
             'module','moment','morris','mostly','mother','motion','moving',
             'murder','museum','mutual','myself','narrow','nation','native',
             'nature','nearby','nearly','nights','nobody','normal','notice',
             'notion','number','object','obtain','office','offset','online',
             'option','orange','origin','output','oxford','packed','palace',
             'parent','partly','patent','people','period','permit','person',
             'phrase','picked','planet','player','please','plenty','pocket',
             'police','policy','prefer','pretty','prince','prison','profit',
             'proper','proven','public','pursue','raised','random','rarely',
             'rather','rating','reader','really','reason','recall','recent',
             'record','reduce','reform','regard','regime','region','relate',
             'relief','remain','remote','remove','repair','repeat','replay',
             'report','rescue','resort','result','retail','retain','return',
             'reveal','review','reward','riding','rising','robust','ruling',
             'safety','salary','sample','saving','saying','scheme','school',
             'screen','search','season','second','secret','sector','secure',
             'seeing','select','seller','senior','series','server','settle',
             'severe','sexual','should','signal','signed','silent','silver',
             'simple','simply','single','sister','slight','smooth','social',
             'solely','sought','source','soviet','speech','spirit','spoken',
             'spread','spring','square','stable','status','steady','stolen',
             'strain','stream','street','stress','strict','strike','string',
             'strong','struck','studio','submit','sudden','suffer','summer',
             'summit','supply','surely','survey','switch','symbol','system',
             'taking','talent','target','taught','tenant','tender','tennis',
             'thanks','theory','thirty','though','threat','thrown','ticket',
             'timely','timing','tissue','toward','travel','treaty','trying',
             'twelve','twenty','unable','unique','united','unless','unlike',
             'update','useful','valley','varied','vendor','versus','victim',
             'vision','visual','volume','walker','wealth','weekly','weight',
             'wholly','window','winner','winter','within','wonder','worker',
             'wright','writer','yellow']
words_seven = ['ability', 'absence', 'academy', 'account', 'accused', 'achieve',
               'acquire', 'address', 'advance', 'adverse', 'advised', 'adviser',
               'against', 'airline', 'airport', 'alcohol', 'alleged', 'already',
               'analyst', 'ancient', 'another', 'anxiety', 'anxious', 'anybody',
               'applied', 'arrange', 'arrival', 'article', 'assault', 'assumed',
               'assured', 'attempt', 'attract', 'auction', 'average', 'backing',
               'balance', 'banking', 'barrier', 'battery', 'bearing', 'beating',
               'because', 'bedroom', 'believe', 'beneath', 'benefit', 'besides',
               'between', 'billion', 'binding', 'brother', 'brought', 'burning',
               'cabinet', 'caliber', 'calling', 'capable', 'capital', 'captain',
               'caption', 'capture', 'careful', 'carrier', 'caution', 'ceiling',
               'central', 'centric', 'century', 'certain', 'chamber', 'channel',
               'chapter', 'charity', 'charlie', 'charter', 'checked', 'chicken',
               'chronic', 'circuit', 'classes', 'classic', 'climate', 'closing',
               'closure', 'clothes', 'collect', 'college', 'combine', 'comfort',
               'command', 'comment', 'compact', 'company', 'compare', 'compete',
               'complex', 'concept', 'concern', 'concert', 'conduct', 'confirm',
               'connect', 'consent', 'consist', 'contact', 'contain', 'content',
               'contest', 'context', 'control', 'convert', 'correct', 'council',
               'counsel', 'counter', 'country', 'crucial', 'crystal', 'culture',
               'current', 'cutting', 'dealing', 'decided', 'decline', 'default',
               'defence', 'deficit', 'deliver', 'density', 'deposit', 'desktop',
               'despite', 'destroy', 'develop', 'devoted', 'diamond', 'digital',
               'discuss', 'disease', 'display', 'dispute', 'distant', 'diverse',
               'divided', 'drawing', 'driving', 'dynamic', 'eastern', 'economy',
               'edition', 'elderly', 'element', 'engaged', 'enhance', 'essence',
               'evening', 'evident', 'exactly', 'examine', 'example', 'excited',
               'exclude', 'exhibit', 'expense', 'explain', 'explore', 'express',
               'extreme', 'factory', 'faculty', 'failing', 'failure', 'fashion',
               'feature', 'federal', 'feeling', 'fiction', 'fifteen', 'filling',
               'finance', 'finding', 'fishing', 'fitness', 'foreign', 'forever',
               'formula', 'fortune', 'forward', 'founder', 'freedom', 'further',
               'gallery', 'gateway', 'general', 'genetic', 'genuine', 'gigabit',
               'greater', 'hanging', 'heading', 'healthy', 'hearing', 'heavily',
               'helpful', 'helping', 'herself', 'highway', 'himself', 'history',
               'holding', 'holiday', 'housing', 'however', 'hundred', 'husband',
               'illegal', 'illness', 'imagine', 'imaging', 'improve', 'include',
               'initial', 'inquiry', 'insight', 'install', 'instant', 'instead',
               'intense', 'interim', 'involve', 'jointly', 'journal', 'journey',
               'justice', 'justify', 'keeping', 'killing', 'kingdom', 'kitchen',
               'knowing', 'landing', 'largely', 'lasting', 'leading', 'learned',
               'leisure', 'liberal', 'liberty', 'library', 'license', 'limited',
               'listing', 'logical', 'loyalty', 'machine', 'manager', 'married',
               'massive', 'maximum', 'meaning', 'measure', 'medical', 'meeting',
               'mention', 'message', 'million', 'mineral', 'minimal', 'minimum',
               'missing', 'mission', 'mistake', 'mixture', 'monitor', 'monthly',
               'morning', 'musical', 'mystery', 'natural', 'neither', 'nervous',
               'network', 'neutral', 'notable', 'nothing', 'nowhere', 'nuclear',
               'nursing', 'obvious', 'offense', 'officer', 'ongoing', 'opening',
               'operate', 'opinion', 'optical', 'organic', 'outcome', 'outdoor',
               'outlook', 'outside', 'overall', 'pacific', 'package', 'painted',
               'parking', 'partial', 'partner', 'passage', 'passing', 'passion',
               'passive', 'patient', 'pattern', 'payable', 'payment', 'penalty',
               'pending', 'pension', 'percent', 'perfect', 'perform', 'perhaps',
               'phoenix', 'picking', 'picture', 'pioneer', 'plastic', 'pointed',
               'popular', 'portion', 'poverty', 'precise', 'predict', 'premier',
               'premium', 'prepare', 'present', 'prevent', 'primary', 'printer',
               'privacy', 'private', 'problem', 'proceed', 'process', 'produce',
               'product', 'profile', 'program', 'project', 'promise', 'promote',
               'protect', 'protein', 'protest', 'provide', 'publish', 'purpose',
               'pushing', 'qualify', 'quality', 'quarter', 'radical', 'railway',
               'readily', 'Reading', 'reality', 'realize', 'receipt', 'receive',
               'recover', 'reflect', 'regular', 'related', 'release', 'remains',
               'removal', 'removed', 'replace', 'request', 'require', 'reserve',
               'resolve', 'respect', 'respond', 'restore', 'retired', 'revenue',
               'reverse', 'rollout', 'routine', 'running', 'satisfy', 'science',
               'section', 'segment', 'serious', 'service', 'serving', 'session',
               'setting', 'seventh', 'several', 'shortly', 'showing', 'silence',
               'silicon', 'similar', 'sitting', 'sixteen', 'skilled', 'smoking',
               'society', 'somehow', 'someone', 'speaker', 'special', 'species',
               'sponsor', 'station', 'storage', 'strange', 'stretch', 'student',
               'studied', 'subject', 'succeed', 'success', 'suggest', 'summary',
               'support', 'suppose', 'supreme', 'surface', 'surgery', 'surplus',
               'survive', 'suspect', 'sustain', 'teacher', 'telecom', 'telling',
               'tension', 'theatre', 'therapy', 'thereby', 'thought', 'through',
               'tonight', 'totally', 'touched', 'towards', 'traffic', 'trouble',
               'turning', 'typical', 'uniform', 'unknown', 'unusual', 'upgrade',
               'upscale', 'utility', 'variety', 'various', 'vehicle', 'venture',
               'version', 'veteran', 'victory', 'viewing', 'village', 'violent',
               'virtual', 'visible', 'waiting', 'walking', 'wanting', 'warning',
               'warrant', 'wearing', 'weather', 'webcast', 'website', 'wedding',
               'weekend', 'welcome', 'welfare', 'western', 'whereas', 'whereby',
               'whether', 'willing', 'winning', 'without', 'witness', 'working',
               'writing', 'written']
words_eight = []

x = 10
y = 20
number_of_words = 10

punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '"',
               '{', '}', '[', ']', '+', '=', '?', '/', '>', '<', '~', '|', ',']


def create_grid(x, grid):
    '''Create string version of grid'''
    for level in range(0, x):
        print(''.join(map(str, grid[level])))


def back_fill(array):
    '''Fill with random'''
    for (x, y), value in np.ndenumerate(array):
        if value:
            continue
        array[x, y] = random.choice(punctuation)
    return array


def create_index(array):
    counter = 1
    index = {}
    for (x, y), value in np.ndenumerate(array):
        index[counter] = x, y
        counter += 1
    return index


def check_word(answer, attempt):
    number_correct = 0
    to_check = answer
    for letter in attempt:
        if letter in to_check:
            number_correct += 1
            to_check = to_check.replace(letter, '')
    return number_correct


def create_starting_points(grid_index, length_of_word, words):
    starting_points = random.sample(range(len(grid_index) - length_of_word), len(words))
    starting_points.sort()
    diffs = [j-i for i, j in zip(starting_points[:-1], starting_points[1:])]
    for i in diffs:
        if i < length_of_word + 1:
            return create_starting_points(grid_index, length_of_word, words)
    return starting_points


@app.route("/")
def main():
    main_grid = np.full((x, y), '')
    difficulty = int(input('Select difficulty (1,2,3,4): '))
    print('\n')
    diff_dict = {1: words_four, 2: words_five, 3: words_six, 4: words_seven, 5: words_eight}
    words = random.sample(diff_dict[difficulty], number_of_words)
    length_of_word = len(words[0])
    grid_index = create_index(main_grid)
    starting_points = create_starting_points(grid_index, length_of_word, words)
    for item in range(len(words)):
        word = [letter for letter in words[item]]
        starting_point = starting_points[item]
        main_grid[grid_index[starting_point]] = word[0]
        for i in range(1, len(word)):
            main_grid[grid_index[starting_point + i]] = word[i]
    back_fill(main_grid)
    create_grid(x, main_grid)
    print('\n')
    answer = random.choice(words)
    no_chances = 3
    while no_chances > 0:
        guess = input('What word? ')
        if guess not in words:
            print('Invalid input. Retry.')
            continue
        if guess == answer:
            print('Access granted.')
            again = input('Again? ')
            if again == 'Y'.lower():
                main()
        else:
            print('Number of correct letters: {}'.format(check_word(guess, answer)))
            no_chances -= 1
            if no_chances == 0:
                print('System locked.')
                again = input('Again? ')
                if again == 'Y'.lower():
                    main()


if __name__ == '__main__':
    main()
