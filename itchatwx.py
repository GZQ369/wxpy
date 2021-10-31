from __future__ import unicode_literals
from threading import Timer
# from wxpy import *
import re
import requests
import datetime as dt
import random
# bot = Bot(cache_path=True)
# console_qr=True,
# bot = Bot(console_qr=Ture, cache_path=Ture) #这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为bot=Bot()
greetList = ['春水初生,春林初盛,春风十里,不如你。',
 '外面风大，跟我回家。',
 '留在我身边，远近我都接受。',
 '向来没耐心的我，在你身边徘徊了这么久。',
 '你站的方向风吹过来都是暖的。',
 '你陪着我的时候，我从来没有羡慕过任何人。',
 '因为有你我才能笑着摇头拒绝所有诱惑和暧昧。',
 '我喜欢你只有一个理由，你就是理由。',
 '你快乐所以我快乐，快乐都是你给的。',
 '如果你最后一贫如洗，我将是你最后的行李。',
 '遇见你是所有故事的开始。',
 '陪我走走吧，趁天还没亮浓雾里还透着光。',
 '我也憧憬过，也怕后来没结果。',
 '所有的不愉快都改变不了我对你的坚持。',
 '你在身边，世界只剩一个焦点。',
 '陪你走到底只要你愿意。',
 '我没有信仰。对于我，你比信仰重要。',
 '如果你能真诚的为我张开快乐，我愿意抛弃一切为你执着。',
 '你可知道你的名字解释了我的一生。',
 '我这一途所遇风景太多，却也不抵你眼。只盼化身一尾黑纹金鱼，栖于你眉目。不惧终成一个溪水枯竭的结局，只怕你无人相伴。',
 '我没有很刻意的去想念你，因为我知道，遇到了就应该感恩，路过了就需要释怀。我只是在很多很多的小瞬间想起你，比如一部电影，一首歌，一句歌词，一条马路和无数个闭上眼睛的瞬间。',
 '原来你是我最想留住的幸运。',
 '如果我说不吻你不罢休，谁能逼我将就。',
 '一次就好，我带你去看天荒地老。',
 '我为你翻山越岭，却无心看风景。',
 '就算今天我把话说的再绝，明天醒来还是会喜欢你，我多没出息这你知道。',
 '如果全世界都对你恶语相加，我就对你说上一世情话。',
 '除了你，万敌不倾。',
 '没关系你也不用给我机会，反正我还有一生来浪费。',
 '回头我就在。',
 '你是雾你是旧梦，你是写在烟盒上的诗，你是我心上的一间小酒馆。',
 '为你，千千万万遍，就让我等一等再放弃。',
 '不希望你被太多人喜欢，我喜欢就好。',
 '哪有什么突然想起你，其实一直在心里。',
 '只要见到你，无论多糟，我都会笑。',
 '我想用余生为你暖一盏茶，晚风微扬时勿忘归家。',
 '你是烈酒，入喉汹涌，一口咽不下，余生慢慢尝。',
 '若有朝一日无处可去，不妨归来，把我当做岁月的尽头。'
 '待在我身边，我怕你危险。',
 '只尊你为王，为你披荆斩棘战四方。',
 '我命由你不由天。',
 '我从不说情话，我对你的每一句话每一个字，都是肺腑之言。',
 '与你相携途中，一切皆为风景。',
 '你的名字是多美的情诗。',
 '遇一人白头，择一城终老。',
 '星辰点缀在你肩上，你眼中有整片海洋。',
 '最好的幸福是你给的在乎。',
 '一辈子只面对一个人，想想就可怕。但是如果是眼前这个人的话，我想我可以赌一下。',
 '若能与君相共度，又何惧荆棘载途。',
 '曾引相思种，春来希盛开，穷冬驱不去，卿在万里外。',
 '愿陪你从天光乍破，走到暮雪白头。',
 '你若撒野，今生我把酒奉陪。',
 '哪怕你受尽千夫所指，我亦护定你。',
 '你走，我不送你。你来，无论多大风多大雨，我要去接你。',
 '你的过去我来不及参与，你的未来我奉陪到底。',
 '何其有幸，此生遇到你。',
 '生命那么短，世界那么乱，我不想争吵，不想冷战，不愿和你有一秒遗憾。',
 '余生请你多指教。',
 '我不怕天黑和惊雷，只怕你心酸和皱眉。',
 '不是因为我执着，而是因为你值得。',
 '每一次我想你，全世界每一处都是你。',
 '你没那么好，只是谁都替代不了。',
 '你拿枪指着我的胸口，就算枪响我也相信只是走火。',
 '时光温热，岁月静好。你还没来，我怎敢老。',
 '只要你的目光还注视着我，我的眼里就永远走不进别人。',
 '如过没有你，明天不值得期待，昨天不值得回忆。',
 '你是我不喜欢别人的理由。',
 '千山万水任时光后退，也只希望在你身边徘徊。',
 '你可知我百年的孤寂只为你一人守候，千年的恋歌只为你一人而唱。',
 '我一生中最美好的时光是，当我和你成为“我们”。',
 '以诗为梦马，以你为年华。',
 '介意你的好多缺点却又统统妥协接受。',
 '不是除了你我就没人要，只是除了你我谁都不想要。',
 '只要你一直在我身边，其他东西不再重要。',
 '傻笑不是与生俱来的，而是由我爱上你的那一刻开始的。',
 '我希望这个世界可以很小很小，小到我一转身就可以看见你。',
 '我不想做你生命的插曲，只想做你生命最完美的结局。',
 '纵然有百万个理由离开你，我也会寻找一个理由为你留下。',
 '希望吹过我的风还能绕几圈去拥抱你。',
 '听说晚安是最情长的告白，但我只知道早安是最深情的问候。',
 '我哪有什么好脾气，我的好脾气，还不是因为爱你。',
 '一辈子有多少来不及我不管，庆幸的是我来得及爱你。',
 '如果我的未来有你在，那其他的什么我都不怕了。',
 '情话很多，我只想与你细水长流。',
 '你若不离，我亦不弃。',
 '万千灯火，就是看上了你。',
 '我喜欢春天的花夏天的树秋天的黄昏冬天的太阳和每天的你。',
 '我给不了你太多，但有个词叫尽我所能。',
 '你在人潮里不知所措，我却跟在你身后，伸手怕犯错，缩手怕错过。',
 '我感觉我是世界上眼光最好的人，因为我看上了你。',
 '总觉得用一个脑袋想你是不够的。',
 '为什么这么多人中偏偏是你，也许是那天阳光正好，微风不燥，你也刚好在笑。',
 '现在想想，我爱你就像，天刮风，云下雨，没有理由没有征兆的就来了。',
 '我是个很慢热的人，但我保温性能很好，一旦热起来，就不会凉下去，比如我喜欢你。',
 '人潮好拥挤，我却只想爱你。',
 '你不需要多好，我喜欢就好。',
 '你一百种样子，我一百种喜欢。',
 '我希望十年后有一场婚礼的主角是你和我，我对着你说我愿意。',
 '若有幸来世再见，长路携手，岁月悠悠，你说从头就从头。',
 '你的名字就几笔，却贯穿了我整个年华。',
 '我不想和别人拥抱，因为那里没有你的心跳。',
 '第一眼就心动的人要怎么做朋友。',
 '我心里数落了你千万条缺点，却抵不过看到你的那一眼。',
 '我向来口笨唇拙，除了爱你什么都不会说。',
 '我必须要看过最蓝的天，爬过最高的山，路过最大的草原，听过最澎湃的海潮声，才有资格说在这个世界上，我最想呆在你身边。',
 '纵然万劫不复，纵然相思入骨，我也待你眉眼如初，岁月如故。',
 '我不想要输赢自尊虚荣了，我想要你。',
 '熬过山头不知风霜的春秋，正午时分我来叩门，走吧，我们去流浪。',
 '等你走到有些累了的时候，我还会借你我的左肩。',
 '在有生的瞬间能遇到你，竟花光我所有运气。',
 '愿山野都有雾灯，你手持火把渡岸而来点亮我孤妄的青春，此后夜车不再驶往孤站，风雨漂泊都能归舟。',
 '一百年很久，有的是时间，每一笔我都不想错过，每一分都不舍抵赖。',
 '慢下来，不要太快，不要怕晚，我们一起拨乱算珠，这一笔互相打个欠条，带进坟墓里，带进来生的记忆里，下辈子，再继续算。',
 '我曾以为我孤独长命，却仍能有幸与你同行在漫长缺氧的枯朽之年的罅隙里。',
 '我爱你胜过爱我自己。',
 '你若觉得高处不胜寒，我便拱手江山讨你欢。',
 '我拒绝更好更圆的月亮，拒绝未知的疯狂，拒绝声色的张扬，不拒绝你。',
 '你是薄雾，是暖风，我喜你依旧浓。',
 '与君初相识，犹如旧人归。',
 '你说人山人海边走边爱怕什么孤单，我说人潮汹涌都不是你该怎么将就。',
 '如果我不曾见过你，我本可以忍受黑暗。如果我不曾遇到你，我本可以一个人也过得很好。',
 '你就像一个信仰，再痛也会向往。',
 '我有孤独和酒，你跟不跟我走？',
 '每天都忍不住去想你，这算不算习惯。',
 '玫瑰是偷的，但爱你是真的。',
 '不想说醉人的情话，我只想带你回家。',
 '如果有你在前方，路再坎坷都是旅行。',
 '即使身边世事再毫无道理，与你永远亦连在一起。',
 '你是我三十九度的风，风一样的梦。',
 '我希望你可以是我的独家记忆。',
 '愿岁月可回首，且以深情共白头。',
 '人来人往我在你身后，张望多久都无妨。',
 '如果所有土地连在一起，走上一生只为拥抱你。',
 '余生太长，你好难忘。',
 '爱经不起遗憾的事，身边的人不可以不是你。',
 '你口中的风景我都觉得好美丽，不过是因为我喜欢你。',
 '我想听你所有的故事，好的坏的，一切。',
 '手的另一边伸给你牵，向南向北我都情愿。',
 '不为日子皱眉头，答应你，只为吻你才低头。',
 '要我等你多久，十个春天够不够？',
 '想听你说情话，抱着你看雪花。',
 '我以为除了你，我喝什么都喝不醉。可好像世间万物又都掺着你，我呼吸会醉，沉默也醉。',
 '若是你看倦了风景，走累了路，我愿意变成酒色的石头，让你把余生靠一靠。',
 '愿你洗去白天的浮躁不安，愿你在每个夜里都能安然入睡美梦相伴。',
 '很多东西看久了都会腻，唯独你，越看越欢喜。',
 '我一生荒芜，唯记得同你在一起时笑的盎然肆意，哭的酣畅淋漓。',
 '你是海，是归船，是遍山翠藤，是诗人的眼泪，是黄昏树梢上挂着的那朵夕阳，是这世间所有美好事物的代表。',
 '灼灼桃花十里，只取你一朵放在心上足矣。',
 '你知道什么叫意外吗，就是我从没想过会遇见你，但我遇见了；我从没想过会爱你，但我爱了。',
 '我在想你收到我的短信，你会不会粲然一笑，就像我收到你的信息一样开心。',
 '每段青春都会苍老，但我希望记忆里的你一直都好。',
 '有些歌听前奏就爱上了，有些作业打开第一页就不想做了，有些人看第一眼就爱上了，比如你。',
 '喜欢天空的颜色大海的深度和你的声音。',
 '你是我穷极一生做不完的一场梦。',
 '深林时见鹿，海蓝时见鲸，梦醒时见你。',
 '你的名字，你的眼睛，你的笑，你的好。我没忘，没敢忘，也没想忘。',
 '你给我半点微笑，我都当个宝，想要炫耀。',
 '我不想和你放荡不焉浪完青春，只想和你安安稳稳到枕边人。',
 '你总有一天会知道，来往的人中，我是最爱你的。',
 '你发的“嗯”都比别人的好看。',
 '除了你再也没有人能住进我的眼睛。',
 '想带着你走过春秋，穿过清晨雨露，傍晚云霞，历经沧桑人世，而我依旧爱你如初。',
 '你在我后半生的城市里。',
 '我爱你，不只是说说而已。',
 '纵使喝醉酒满嘴胡话，也有一句好想你是发自肺腑。',
 '你是我期待又矛盾的梦想，抓住却不能拥抱的风，想喝又怕醉的酒。',
 '我放你去浪，等你尝过所有新鲜感，等你终于感到了厌倦，我还等你呢。',
 '我没有讨好你的天分，但我比谁都认真。',
 '我身边并不拥挤，你来了就是唯一。',
 '你是我的梦，像北方的风。',
 '我曾经风沙尘土一马一夕，忘记所有人却唯独爱上你。',
 '你一笑我高兴很多天，你一句话我记好多年。',
 '我行过许多地方的桥，看过许多次数的云，喝过许多种类的酒，却只爱过一个正当最好年龄的人。',
 '你是我光是想想都会偷着乐的人。',
 '我最喜欢的一个字是吃，两个字是旅行，三个字是你名字。',
 '你三三两两的醉语，我将嗔痴一饮而尽。',
 '你一直住在我的心里久到变成了房东。',
 '我从远方赶来，恰好你也在。',
 '我不喜欢这个世界，但我喜欢你。',
 '喜你是疾，药石无医。',
 'Will you be my lover？',
 ' Will you be the one？',
 '最好闻的是，抱你时你身上的味道。',
 '好像你说什么都是好听的，可以淡化悲伤，也能燃起热潮。',
 '不敢凝视你的眼睛，是怕我每个眼神都在表白。',
 '春天会下雪，夏天有大雨，秋天会起风，冬天有艳阳。一年四季会有很多意外，但最迷人的，还是遇见了你。',
 '只要你在身边，去哪里都是风景。',
 '你所有为人称道的美丽，都不及我第一次遇见你。',
 '我见过千万人，像你的发，像你的眼，但都不是你的脸。',
 '因为爱你，所以看谁都像情敌。',
 '我不知道我为什么爱你，就像我无法描述水是什么味道一样。但我知道我需要你，就像我需要水一样。',
 '我本来打算告诉你，当你不在我身边时，我所遇到的所有糟糕事。但最后，我只想告诉你，我很想你。',
 '世界上最短的咒语，是你的名字。',
 '喜欢你，就是心里放弃了一千次也会在你说一句好听的话再奋不顾身一万次。',
 '很多时候我对一个人的喜欢就像是兜里揣了一块糖，想跟别人显摆，又不想给别人吃。',
 '你应该被抱紧，有风我来顶。',
 '我愿拿青春换酒共你白头。',
 '最在乎的人，最重视的人，最特别的人，最珍惜的人，都是同一个你。',
 '无论我变得如何强大，你仍然是我的弱点。',
 '每一次我想你，全世界每一处都是你。',
 '自从认识了你，我就没打算忘了你。',
 '我以为我百毒不侵，却唯独对你上了瘾。',
 '世间的五味俱全，谢谢你给我的甜。',
 '不羁岁月磨白头，一个你一壶酒，便是盼头。',
 '陪你走的青春是我一生一次的认真。',
 '你知我从未惧怕奔赴，不过是因为你在路的尽头。',
 '修你一世平安喜乐，护你百岁无忧安康。',
 '没有你，良辰美景更与何人说。',
 '我们路过多少风景，看过多少路标，多少故事藏在心里，多少言语无人倾听。咖啡换了第几杯，身旁经过多少人，心里藏着的那些歌，想唱给的人都是你。',
 '我想不出来第一次看见你的时候，你穿的衣服是什么颜色。是晴天还是雨天，因为我从未想到那天之后我会喜欢你。',
 '天空很蓝，风很凉爽，景很动人，好看的人更多，但所有的这些，都不及你。',
 '我不怕老，也不怕死，只怕我所深爱的你过得不好。',
 '车马很慢，阳光很懒，你很好看。',
 '就算大雨让整座城市颠倒，我会给你怀抱。','快去睡觉别熬夜','好好工作,工作加油','注意身体多喝热水','想你了求自拍','天干物燥，小心火烛']
lelist=[
 '第一封：既见君子，云胡不喜？',
 '第二封：玲珑骰子安红豆，入骨相思君知否？',
 '第三封：世人谓我恋长安，其实只恋长安某。',
 '第四封：山有木兮木有枝，心悦君兮君不知。',
 '第五封：一往情深深几许，深山夕照深秋雨。',
 '第六封：长相思兮长相忆，短相思兮无穷极。',
 '第七封：早知如此绊人心，何如当初莫相识。',
 '第八封：朝暮不依长相思，白首不离长相守。',
 '第九封：来世你渡我，可愿？',
 '第十封：一世红尘，无你何欢？',
 '第十一封：此情无计可消除，才下眉头，却上心头。',
 '第十二封：灼灼桃花，三千繁华，却似人间只有一个他。',
 '第十三封：百千夜尽，谁为我，化青灯一座，谁倚门独望过千年烟火。',
 '第十四封：如若今生再相见，哪怕流离百世，迷途千年，也愿。',
 '第十五封：我一觉醒转，你一定就在彼岸一壶茶，等一树桃花。',
 '第十六封：鸿雁在云鱼在水，惆怅此情难寄。',
 '第十七封：有尔存焉，得尔我幸。',
 '第十八封：平生不会相思，才会相思，便害相思。',
 '第十九封：老来多健忘，唯不忘相思。',
 '第二十封：黄泉路上，忘川河上，三生石旁，奈何桥上，我可曾见过你？',
 '第二十一封：春风十里不如你。',
 '第二十二封：依依目光，此生不换。',
 '第二十三封：以我浮生，渡君一梦。',
 '第二十四封：陌上花开，可缓缓归矣。',
 '第二十五封：青山不老，与君白头。',
 '第二十六封：那年桃夭，红豆暗抛。',
 '第二十七封：昔我往矣，杨柳依依。',
 '第二十八封：浮生若梦，不负初情。',
 '第二十九封：提一盏灯笼，迎着风雨寻你。',
 '第三十封：红尘万丈，只为渡你而来。',
 '第三十一封：此心安处是吾乡。',
 '第三十二封：此生等候，只为你刹那回眸。',
 '第三十三封：梧桐深处凤未归。',
 '第三十四封：君去后，酒暖思念瘦。',
 '第三十五封：只愿君心似我心。',
 '第三十六封：当时明月在，曾照彩云归。',
 '第三十七封：愿得一心人，白首莫相离。',
 '第三十八封：情不知所起，一往而深。',
 '第三十九封：待到繁花落尽，与你细水长流。',
 '第四十封：执子之手，与子偕老。',
 '第四十一封：生死契阔，与子成说。',
 '第四十二封：一日不见，如三秋兮。',
 '第四十三封：青青子衿，悠悠我心。',
 '第四十四封：寄君一曲，不问曲终人聚散。',
 '第四十五封：只缘感君一回顾，使我思君朝与暮。',
 '第四十六封：扶门切思君之嘱，登高望断天涯路。',
 '第四十七封：但愿人长久，千里共婵娟。',
 '第四十八封：待我长发及腰，少年娶我可好？',
 '第四十九封：衣带渐宽终不悔，为伊消得人憔悴。',
 '第五十封：日不见兮，思之如狂。',
 '第五十一封：两情若是久长时，又岂在朝朝暮暮。',
 '第五十二封：曾经沧海难为水，除却巫山不是云。',
 '第五十三封：身无彩凤双飞翼，心有灵犀一点通。',
 '第五十四封：在天愿作比翼鸟，在地愿为连理枝。',
 '第五十五封：人生若只如初见。',
 '第五十六封：当时只道是寻常。',
 '第五十七封：我愿执笔弃花间，从此以后，离经易道，只为你。',
 '第五十八封：天下人何限，慊慊独为汝。',
 '第五十九封：上邪，我欲与君相知，长命无绝期。',
 '第六十封：剪不断，理还乱。',
 '第六十一封：月上柳梢头，人约黄昏后。',
 '第六十二封：门前一树紫荆花。',
 '第六十三封：与君初相识，犹如故人归。',
 '第六十四封：愿君多采撷，此物最相思。',
 '第六十五封：此情可待成追忆。',
 '第六十六封：盈盈一水间，脉脉不得语。',
 '第六十七封：郎骑竹马来，绕床弄青梅。',
 '第六十八封：一起不思量，也攒眉千度。',
 '第六十九封：上穷碧落下黄泉。',
 '第七十封：春蚕到死丝方尽，蜡炬成灰泪始干。',
 '第七十一封：斑竹枝，斑竹枝，泪痕点点寄相思。',
 '第七十二封：胜却人间无数。',
 '第七十三封：投我以求桃，报之以琼瑶。',
 '第七十四封：人生自是有情痴，此恨不关风与月。',
 '第七十五封：今夕何夕，见此良人。',
 '第七十六封：一川烟草，满城风絮，梅子黄时雨。',
 '第七十七封：思君如满月，夜夜减清晖。',
 '第七十八封：月明人倚楼。',
 '第七十九封：生当复来归，死当长相思。',
 '第八十封：你春衫年少，我桃之夭夭。',
 '第八十一封：南风未起，念你成疾。',
 '第八十二封：一蓑烟雨任平生。',
 '第八十三封：三生三世，歌尽桃花。',
 '第八十四封：憧憧似有梦，此心谁人知。',
 '第八十五封：泼墨三千烟火，许你一世迷离。',
 '第八十六封：深知身在情长在，怅望江头江水声。',
 '第八十七封：桃花为盟，枯草为冠。',
 '第八十八封：临窗听雨念君安。',
 '第八十九封：一夜东风吹柳绿，满塘碧水映桃红。',
 '第九十封：木槿花开正好。',
 '第九十一封：锦书难托思君意，笔下付尽心中情。',
 '第九十二封：只一眼，便千秋万世。',
 '第九十三封：你听风声，我看云起。',
 '第九十四封：此生如若不是你，何愁青丝配白衣。',
 '第九十五封：君不来，我不愿老去。',
 '第九十六封：白马枯叶总相依。',
 '第九十七封：愿做一支荷，一生只为你亭亭。',
 '第九十八封：落花时节又逢君。',
 '第九十九封：拾尽春花皆是你。',
 '第一百封：以我江山，许你盛景',

 '第一封 外面风大 跟我回家',
 '第二封 留在我身边 远近我都接受',
 '第三封 我没说过永远 只希望每个明天你都在',
 '第四封 南风过境十里春风不如你',
 '第五封 可能时间刚好 你眼角带笑',
 '第六封 定要有你 方为人生',
 '第七封 向来没耐心的我 在你身边徘徊了这么久第八封 任凭风吹也无法忘记你的名字',
 '第九封 你说以后是我和你喝交杯酒还是我去喝你们的喜酒',
 '第十封 我期待我能在有一天背着背包出现在你的城市',
 '第十一封 你站的方向风吹过来都是暖的',
 '第十二封 手不要给别人牵 怀抱也要留给我',
 '第十三封 你陪着我的时候 我从来没羡慕过任何人',
 '第十四封 想你的时候风忽然停了',
 '第十五封 因为有你我才能笑着摇头拒绝所有诱惑和暧昧',
 '第十六封 No one and you.',
 '第十七封 我喜欢你只有一个理由 你就是理由',
 '第十八封 你就像我小时候最喜欢的玩具 别人碰一下我都觉得那是在抢',
 '第十九封 The first glance Heartbeat.',
 '第二十封 遇见你花光了我所有的运气',
 '第二十一封 想去的地方有你才最美丽',
 '第二十二封 喜欢你是我做过最美丽的事',
 '第二十三封 还在我身边就是我的',
 '第二十四封 微风轻轻起 我好喜欢你',
 '第二十五封 你总是能让我带着每天的晚安把梦做到最感动',
 '第二十六封 你快乐所以我快乐我快乐都是你给的',
 '第二十七封 为你上九天揽月 下五洋捉鳖',
 '第二十八封 对谁都三分钟热度 唯独你',
 '第二十九封 喜你为疾 药石无医',
 '第三十封 如果你最后一贫如洗 我将是你最后的行李',
 '第三十一封 就好像太阳不会放弃天空',
 '第三十二封 遇见你是所有故事的开始',
 '第三十三封 我想顺着你的脚步 走向未来',
 '第三十四封 以后去哪都把我给带上 我会很乖不给你添麻烦',
 '第三十五封 天和地和你一个都不能少',
 '第三十六封 见到你我占有欲就超标',
 '第三十七封 我想每天都能见到你 毕竟我真的很粘人',
 '第三十八封 酸涩皱眉与你共苦不算太差',
 '第三十九封 眼睛好疼',
 '第四十封 你是雾是风我喜你依旧浓',
 '第四十一封 陪我走走吧 趁天还没亮浓雾里还透着光',
 '第四十二封 别在我离不开你的时候离开我',
 '第四十三封 你是我口中最为骄傲的语气',
 '第四十四封 街边的每个身影都像你',
 '第四十五封 我也憧憬过也怕后来没结果',
 '第四十六封 抓紧你的手走过我的朝朝暮暮',
 '第四十七封 陪在身边才算拥有',
 '第四十八封 你别皱眉你最珍贵',
 '第四十九封 尽我所能',
 '第五十封 你是前提你是例外',
 '第五十一封 我有我自己你跟不跟我走',
 '第五十二封 好好的待在你身边是我唯一的心愿',
 '第五十三封 我希望每次伸手你都在',
 '第五十四封 我任性也不是对所有人',
 '第五十五封 如除我一人在你心 还多出一个人 瞒住我',
 '第五十六封 念你名字一百遍就出现在我眼前好不好',
 '第五十七封 你的怀抱是我的避风港',
 '第五十八封 喜欢你这些日子就像一本病历',
 '第五十九封 You are the one.',
 '第六十封 喜欢你的故事更喜欢故事里的你',
 '第六十一封 你的一言一行都牵扯着我的情绪',
 '第六十二封 你有多重要我也害怕让你知道',
 '第六十三封 夜空霓虹都是我不要的繁荣',
 '第六十四封 我喜欢你 只是喜欢你哪有什么目的第六十五封 你不在的时候我在忙着长大',
 '第六十六封 所有的不愉快都改变不了我对你的坚持',
 '第六十七封 原谅我有时候注意不了你在意的细节第六十八封 爱过了你就没办法像爱你一样去爱别人',
 '第六十九封 只要你在我身边我就不会迷路',
 '第七十封 遇见你真幸运',
 '第七十一封 等我长大',
 '第七十二封 我没有固执只是不想再过不安定的生活',
 '第七十三封 你在 走到哪里都是童话',
 '第七十四封 最暖不过在你身边',
 '第七十五封 还好我身边的是你',
 '第七十六封 时间挺住 你就永远是我的',
 '第七十七封 初识你名',
 '第七十八封 每天早上醒来 阳光和你都在',
 '第七十九封 我只是一个说谎者 所以我从来都不喜欢你',
 '第八十封 你住在我心里',
 '第八十一封 你的名字',
 '第八十二封 是我见过',
 '第八十三封 最美的情诗',
 '第八十四封 变成一条鱼 一生都不闭眼睛 一直看着你',
 '第八十五封 你留下 或者我跟你走',
 '第八十六封 她们都是提到你 眼睛都在发亮',
 '第八十七封 遇见你是我最美的意外',
 '第八十八封 你在身边世界只剩一个焦点',
 '第八十九封 我把前半生写在纸上',
 '第九十封 后半生写在你的生命里',
 '第九十一封 我的你',
 '第九十二封 从此你在我心里最温暖的地方',
 '第九十三封 我会改掉不好的毛病',
 '第九十四封 喜欢就像一阵风',
 '第九十五封 因为在乎',
 '第九十六封 喜欢你应该是我干过最棒的事',
 '第九十七封 陪你走到底只要你愿意',
 '第九十八封 情书是我抄的，但我喜欢你是真的',
 '第九十九封 套路是我学的，但我喜欢你是真的',
 '第一百封 别再到处流浪 别在深夜买醉 别喝陌生人给的酒 也别牵别人的手',
 ]


def oneDayMsg():

    print("龚志强:",random.sample(greetList, 1)[0])

def get_news1():
    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/ds_open.php?id=59763&name=%E5%8F%8D%E5%80%92%E6%98%AF&auth=2BD25827B51804754DEC1F44EE5E3C34"
    r = requests.get(url)
    content = r.text
    le = re.compile(r'title=".*?\"')
    ls = re.findall(le, content)
    lx = ls[0]
    contents = lx[7:-1]
    #print(contents)
    return contents
# def tick():
#     users = bot.friends().search(u"hid")[0] # 找到你女朋友的名称
#     meetDate = dt.date(2013,9,29)  # 这是你跟你女朋友相识的日期
#     now = dt.datetime.now()     # 现在的时间
#     nowDate = dt.date.today()  # 今天的日期
#     passDates = (nowDate-meetDate).days # 你跟你女朋友认识的天数
#     itchat.send(u'今天是我们认识第%d天，%s,晚安'%(passDates,random.sample(greetList,1)[0]),toUserName=userName) # 发送问候语给女朋友

def send_news(sendfriend,Y,M,D):
    try:
        my_friend = bot.friends().search(sendfriend)[0] # 你朋友的微信昵称，不是备注，也不是微信帐号。"安生。"
        print(my_friend.send(get_news1()))        # 此处获取的是get_news1()方法返回列表的第一部分内容
        #my_friend.send(get_news1()[1][5:])     #词霸小编：野草遮不住太阳的光芒，……，即去掉词霸小编：
        t = Timer(86400, send_news)     # 每86400秒（1天），发送1次，不用linux的定时任务是因为每次登陆都需要    扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
        meetDate = dt.date(Y,M,D)#2015, 3, 15)#        #  # 这是你跟你女朋友相识的日期
        now = dt.datetime.now()  # 现在的时间
        nowDate = dt.date.today()  # 今天的日期
        passDates = (nowDate - meetDate).days  # 你跟你女朋友认识的天数
        print(my_friend.send('今天是我们认识第%d天.%s晚安!' % (passDates, random.sample(greetList, 1)[0])))  # 发送问候语给女朋友
        #print('今天是我们认识第%d天.%s晚安!' % (passDates, random.sample(greetList, 1)[0]))
        print(my_friend.send('不好意思，给你的信因为台风来了给刮走了几天！所以今天给你的一百封信是--%s' % (random.sample(lelist, 1)[0])))
        #print('给你的一百封信--%s' % (random.sample(lelist, 1)[0]))
        t.start()
    except:
        my_friend = bot.friends().search("hid")[0]   # 你的微信昵称，不是微信帐号。
        my_friend.send(u"今天消息发送失败了")
        print(u"今天消息发送失败了")
if __name__ == "__main__":
    # send_news("是珮珮啊",2015,3,15)
    # send_news("不爱吃鱼",2013,6,6)
    # send_news("安生",2013,9,29)
    # send_news("hid",2013,9,29)
    # #send_news("17",2017,11,12)将你一
    # #send_news("愛蘿莉真是太",2017,10,19)
    # send_news("糠糠",2015,11,11)
    # send_news("脉搏",2017,9,15)
    oneDayMsg()
