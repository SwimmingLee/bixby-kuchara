# 동네영화관 :popcorn:
갑자기 팝콘이 먹고싶을 때는 동네영화관에서 상영 중인 영화를 찾아보세요!  
동네영화관은 보고싶은 영화를 내 위치 주변의 영화관에서 모두 찾고 한눈에 쉽게 비교할 수 있도록 하여, 빠르게 **내 상황에 맞는 최적의 영화를 고를 수 있도록 도와주는 캡슐**이에요.

### 동네영화관을 통한 영화 예매 과정 비교
기존의 앱을 이용한 영화 예매 방식에서, 사용자는 **최적의 영화 시간**을 찾기 위해 여러번의 클릭과 복수의 앱을 이동하며 최적의 시간을 찾아야 했어요.
동네영화관에서는 자동으로 주변 영화관에서 상영하는 영화를 보여주고, 사용자가 원하는 영화를 클릭하기만 하면 근처 영화관의 상영 시간표를 모아서 한번에 검색해주는 방식으로 그 불편함을 해결할 수 있어요.

<img src= "/kuchara.bomnal/assets/images/Bixby-user-scenario.png" width="100%" height="100%" >

<br>

### 캡슐 사용하기
### :mag_right: [동네영화관 사용설명서](#사용-설명서-metal)
### :mag_right: [부록: 필터링](#부록-필터링-grey_exclamation)

<br>

***

# 사용 설명서 :metal: 

## 동네영화관에서 지금 내 주변에서 상영 중인 영화를 선택하고 예매를 진행해보세요!

### 빅스비에게 말해보세요.

	User	| "동네영화관에서 영화 뭐 하는지 알려줘"
	Bixby	| "근처에서 상영하는 영화들을 알려드릴게요. 먼저 보고 싶은 영화를 선택해주세요."
	User	| (겨울왕국2 클릭)
	Bixby	| "오늘 근처에서 겨울왕국2를 상영하는 영화관과 상영 시간을 알려줄게요. 원하시는 시간을 눌러 영화 정보를 확인해주세요."
	User	| (원하는 상영 시간 클릭)
	Bixby	| "선택하신 영화는 오늘 왕십리CGV에서 상영되는 영화 겨울왕국 2입니다. 웹으로 이동하여 예매를 완료해주세요."

<img src= "/kuchara.bomnal/assets/images/Bixby-use-scenario.png" width="100%" height="100%" >

<br>

## 동네영화관에서 원하는 정보를 찾기 어렵다구요? (설마)

### 원하는 영화정보가 없다면,
#### :point_right: 그 영화는 주변에서 상영하지 않는 영화일 확률이 매우 높아요! 
동네영화관은 자동으로 사용자의 위치를 확인하고 주변에서 볼 수있는 영화들만 보여주기 때문에, 주변에서 상영하지 않는 영화는 아직 고를 수가 없어요.
빅스비가 더욱 더 똑똑해지기 위해 열심히 노력하는 중이니, 다음에는 영화를 고를 수 있는 방법도 공부해볼게요!

> :honey_pot:Tip | 그래도 원하는 영화를 꼭 보고 싶다면 상영하는 영화관을 고른 뒤([다른 영화관 고르는 방법](#다른-영화관을-고르고-싶다면)) 해당 영화정보를 확인해주세요.

<br>

### 원하는 영화관이 결과에 없다면,
#### :point_right: 빅스비에게 다른 영화관을 보여달라고 말해보세요!
빅스비는 사용자 주변의 가장 가까운 영화관들을 차례대로 찾아 상영시간표를 보여주도록 공부했어요.
만약 빅스비가 영화관 별 상영시간표를 보여줬을 때 영화를 보고 싶은 곳이 따로 있거나 근처에 있는 영화관이 나오지 않은 경우에는 다음과 같이 말씀해보세요.  
* 다른 영화관에서 영화를 보고싶다면 `다른 영화관에서 보여줘`라고 말씀해보세요.   
그럼 근처에 있는 다른 영화관들의 목록을 보여줄거예요. 
* 영화를 다른 지역에서 보고 싶다면 원하는 지역을 포함하여 `부산에 있는 영화관에서 보여줘`라고 말씀해보세요.   
그럼 이번에는 해당 지역의 근처에 있는 영화관들의 목록을 보여줄거예요.

> :honey_pot:Tip | 그래도 원하는 영화를 꼭 보고 싶다면 상영하는 영화관을 고른 뒤([다른 영화관 고르는 방법](#다른-영화관을-고르고-싶다면)) 해당 영화정보를 확인해주세요.
> :honey_pot:Tip | 이 방법은 빅스비가 상영시간표를 보여줬을 때 사용할 수 있어요.

<br>

### 원하는 정보만 따로 보고 싶다면 (자세한 정보는 필터링 기준을 클릭하여 확인)
#### :point_right: 상황에 맞게 다양한 필터링을 이용해보세요. 
필터링은 보고싶은 영화를 클릭한 후 결과에 대해 적용 가능하며, 영화에 대한 필터링은 불가능해요. 
영화를 다시 고르고 싶다면, 보고싶은 영화를 재설정해주세요.

| 필터링 대상 | 제공되는 필터 기준 | 이렇게 말씀해보세요. |
|:---------:|:---------:|:----------:|
| 영화관 | [특정 브랜드](#filter-영화관-브랜드) | `메가박스 빼줘` `롯데시네마 것만 볼래` |
| 영화관 | [특별관](#filter-영화관-상영관) | `샤롯데 제외해줘` `아이맥스만 보여줘` |
| 영화관 | [특정 영화관](#filter-영화관-점포) | `성신여대 CGV 빼고 보여줘` `송파 CGV만 보여줘` |
| 상영시간표 | [상영시간 정렬방식](#filter-상영-시간표-정렬방식) | `시간순으로 보여줘` `영화관순으로 보여줘` |
| 상영시간표 | [특정 시간](#filter-상영-시간표-시간) | `10시 전에 시작하는 영화만 알려줘` `밤 9시 이후 영화만 알려줘` |

> :honey_pot:Tip | 영화 점포 필터링은 시간순으로 정렬된 화면에서 유용하게 사용이 가능해요.


<br>
<br>

***
# 부록: 필터링 :grey_exclamation:
## 요약정리
필터링은 현재 **영화관에 관한 필터링**과 **상영시간표 보기 방식**에 관한 필터링을 제공하고 있어요.

| 필터링 대상 | 기준 | 예시 발화 |
|:-----:|:-----:|:-----:|
| 영화관 | [브랜드](#filter-영화관-브랜드) | `롯데시네마 빼고` `메가박스에서만` |
| 영화관 | [상영관](#filter-영화관-상영관) | `샤롯데는 제외해줄래?` `아이맥스에서만 찾아줘` |
| 영화관 | [점포](#filter-영화관-점포) | `성신여대 CGV점 빼고` `송파 CGV에서만 볼래` |
| 상영시간표 | [시간](#filter-상영-시간표-시간) | `저녁 6시 전에 볼 수 있는 영화 알려줘` |
| 상영시간표 | [정렬방식](#filter-상영-시간표-정렬방식) | `(영화관순일 때)시간순으로 보고싶어` `(시간순일 때)영화관순으로 정렬해줘` |

<br>

## 필터링 상세 설명

### [Filter] 영화관: 브랜드
##### :exclamation: 특정 브랜드 영화관만 보거나 제외하고 싶을 때  
특정 영화관 브랜드의 매점을 좋아할 수도 있는 당신을 위한 필터링 기능이에요. 브랜드 필터링 기능은 국내 3사 `CGV` `메가박스` `롯데시네마` 모두 적용 가능하며, 상황에 따라 [점포명으로 필터링](#Filter-영화관-점포)하는 방법과 함께 적재적소에 사용하면 빅스비 마스터가 될 수 있어요. 브랜드명은 모두 적절한 줄임말 사용이 가능해요.

> 패턴 | [브랜드 이름][만/제외하고][보여줘]

* 영화 이름 | `롯데시네마` `롯시` `메가박스` `메박` `씨지비` `CGV` 
* 필터링 실행 명령어 | `~만 보여줘` `~만 볼래` `~빼줘` `~제외하고 보여줘`

######
	"롯데시네마 제외하고 보여줘"
	"메가박스에서만 보여줘"
	"CGV는 빼줘"

> :honey_pot:Tip | 매점 추천메뉴  
> * CGV  |  `죠스튀김범벅` `치즈볼`  
> * 메가박스  |  `통찡어` `치킨앤칩스`  
> * 롯데시네마  |  `와사비마요오징어` `햄에그머핀` 

<br>

### [Filter] 영화관: 상영관
##### :exclamation: 결과에서 특별관의 상영시간표만 보거나 제외할 때  
특별관에서 관람하고 싶은(혹은 그렇지않은) 당신을 위한 필터링 기능이에요. 특별상영관은 화면에서 노란색 박스 아이콘 안에 표기되어 있으며, 몇몇 상영관의 경우 아주 멋진 경험을 할 수 있지만 가격이 크게 달라지기 때문에 상황에 따라 적절하게 필터링을 사용해보세요.

> 패턴 | [상영관 이름][만/제외하고][보여줘]

* 영화 이름 | `샤롯데` `CINE de CHEF` `아이맥스` `컴포트관` `더부티크` 
* 필터링 실행 명령어 | `~만 보여줘` `~만 볼래` `~빼줘` `~제외하고 보여줘`

######
	"샤롯데 제외하고 보여줘"
	"씨네 어쩌고 빼고 보여줘"
	"아이맥스만 보여줘"
	"컴포트관 보여줘"

> :honey_pot:Tip | 이색 상영관(가격)  
> * CGV        | [CINE & FORET(18,000)](http://www.cgv.co.kr/theaters/special/?regioncode=CF)  |  [TEMPUR CINEEMA(2인 8~90,000)](http://www.cgv.co.kr/theaters/special/?regioncode=TEM)  
> * 메가박스     | [더부티크(14,000)](http://www.megabox.co.kr/?menuId=special)  |  [The First Club(30,000)](https://www.megabox.co.kr/?menuId=special-detail&screenType=02&cinema=4112)  
> * 롯데시네마    | [샤롯데(35,000)](http://www.lottecinema.co.kr/LCHS/Contents/Cinema/charlotte-special-cinema.aspx?divisionCode=2&screendivcd=300)  

<br>

### [Filter] 영화관: 점포  
##### :exclamation: 특정 점포만 보거나 제외할 때
다수의 영화관 정보를 포함한 상영시간 확인 시, 명확한 비교를 위해 특정 점포를 제외하거나 특정 점포에서만 정보를 확인하고 싶은 당신을 위한 필터링 기능이에요. `CGV 송파점`처럼 브랜드와 지점명을 붙여 지칭하는 방식으로 필터링 사용이 가능해요.  
**주의** `동대문점만 보여줘` 혹은 `왕십리 지점 제외해줘`라고 하면 영화관 브랜드가 특정되지 않았기때문에 필터링이 불가능해요.

> 패턴 | [지점명][만/제외하고][보여줘]

* 지점명 | `송파 CGV` `CGV 송파점` `메가박스 코엑스` `코엑스 메박` `건대입구 롯데` `롯데시네마 월드타워점`
* 필터링 실행 명령어 | `~만 보여줘` `~만 볼래` `~빼줘` `~제외하고 보여줘`

######
	"롯데시네마 월드타워에서만 보여줘"
	"성신여대점 CGV에서만 보고싶어"
	"메박 코엑스는 빼"

> :honey_pot:Tip | 이 기능은 시간순으로 정렬되어있을 때, 유용하게 사용될 수 있어요.

<br>

### [Filter] 상영 시간표: 시간  
##### :exclamation: 특정 시간 이전/이후의 상영시간표를 보고 싶을 때 
예매 시 영화 시간이 중요한 당신을 위한 필터링 기능이에요. 시간에 `오전` `오후`를 붙이지 않아도 시간 해석이 가능하며, 단순하게 특정 시점 이전/이후 영화를 검색해줄 뿐만 아니라 현재 시간부터 원하는 시간만큼 떨어진 시점의 영화를 검색할 수도 있어요.

> 패턴 | [시간] [이후/이전] 영화 [보여줘]

* 시간 | `저녁 6시` `아침 10시 반` `여덟시 삼십분` `2시간`
* 이후/이전 | `전` `이전에 하는` `전에 시작하는` `이후` `뒤` `지나서 하는`
* 필터링 실행 명령어 | `보여줘` `알려줘` `보고싶어` `예매할래`

######
	"저녁 6시 전에 볼 수 있는 영화 알려줘"
	"아침 11시 지나서 하는 영화 보고싶어"
	"7시 전에 상영하는거 보여줘"
	
> :honey_pot:Tip | `오후 3시 이후 영화`라고 이야기한 뒤에 `오후 7시 이전 영화`라고 다시한번 말하면 **오후 3시부터 7시 사이에 상영하는 영화** 결과를 확인할 수 있습니다. 
	
<br>

### [Filter] 상영 시간표: 정렬방식  

##### :exclamation: 결과를 시간순/영화관순으로 정렬해서 보고 싶을 때  
조금 더 다양하게 비교를 해보고 싶은 당신을 위한 필터링 기능입니다. 빅스비는 기본적으로 영화관 별 상영시간표를 보여주게 되는데, `시간순 정렬방식 필터링`은 이 결과를 시간 축으로 재정렬하여 사용자가 시간을 기준으로 영화를 비교할 수 있도록 도와줍니다. 시간 순으로 정렬한 뒤, 다시 같은 영화관끼리 묶어 정렬하고 싶다면 `영화관순 정렬방식 필터링`을 이용하면 됩니다.

> 패턴 | [정렬방식]으로 [보여줘]

* 정렬방식 | `시간순` `영화관순`
* 필터링 실행 명령어 | `보여줘` `정렬해줘` `정리해줘` `나열해줘`

######
	"시간순으로 보여줘"
	"영화관순으로 보여줘"

> :honey_pot:Tip | 시간순은 **영화관에 상관 없이** 모든 영화를 시간순으로 정렬해주며 영화관순은 **한 영화관에서** 상영중인 영화를 시간순으로 정렬해줍니다.


<br>

***

<img src= "/kuchara.bomnal/assets/images/Icon.png" width="10%" height="10%" >

<br>
