(define (problem emergency) (:domain exit)
(:objects
exit_b center exit_a crossroad_1 crossroad_2 bog_and_ide crossroad_3 crossroad_4 crossroad_5 crossroad_6 crossroad_7 crossroad_8 toilets crossroad_13 crossroad_14 crossroad_15 paw_sko smart_eyes exit_c nails_gallery bella_donna crossroad_16 big_hall crossroad_17 exit_d crossroad_18 synoptik change  - nodes
exit_b-crossroad_1 center-crossroad_2 center-crossroad_3 center-crossroad_5 center-crossroad_8 center-crossroad_7 exit_a-crossroad_4 exit_a-crossroad_6 crossroad_1-exit_b crossroad_1-crossroad_4 crossroad_1-crossroad_2 crossroad_2-crossroad_1 crossroad_2-center crossroad_2-toilets bog_and_ide-crossroad_3 crossroad_3-center crossroad_3-bog_and_ide crossroad_3-crossroad_4 crossroad_4-crossroad_1 crossroad_4-crossroad_3 crossroad_4-exit_a crossroad_5-center crossroad_5-crossroad_6 crossroad_6-crossroad_5 crossroad_6-crossroad_13 crossroad_6-exit_a crossroad_7-center crossroad_7-crossroad_17 crossroad_8-center crossroad_8-crossroad_14 toilets-crossroad_2 crossroad_13-crossroad_6 crossroad_13-smart_eyes crossroad_13-big_hall crossroad_14-crossroad_8 crossroad_14-paw_sko crossroad_14-crossroad_15 crossroad_15-crossroad_14 crossroad_15-nails_gallery crossroad_15-bella_donna crossroad_15-crossroad_16 paw_sko-crossroad_14 smart_eyes-crossroad_13 exit_c-crossroad_16 nails_gallery-crossroad_15 bella_donna-crossroad_15 crossroad_16-crossroad_15 crossroad_16-exit_c big_hall-crossroad_13 big_hall-exit_d big_hall-crossroad_18 crossroad_17-crossroad_7 crossroad_17-crossroad_18 crossroad_17-change exit_d-big_hall crossroad_18-big_hall crossroad_18-crossroad_17 crossroad_18-synoptik synoptik-crossroad_18 change-crossroad_17 exit_b-exit_b center-center exit_a-exit_a crossroad_1-crossroad_1 crossroad_2-crossroad_2 bog_and_ide-bog_and_ide crossroad_3-crossroad_3 crossroad_4-crossroad_4 crossroad_5-crossroad_5 crossroad_6-crossroad_6 crossroad_7-crossroad_7 crossroad_8-crossroad_8 toilets-toilets crossroad_13-crossroad_13 crossroad_14-crossroad_14 crossroad_15-crossroad_15 paw_sko-paw_sko smart_eyes-smart_eyes exit_c-exit_c nails_gallery-nails_gallery bella_donna-bella_donna crossroad_16-crossroad_16 big_hall-big_hall crossroad_17-crossroad_17 exit_d-exit_d crossroad_18-crossroad_18 synoptik-synoptik change-change  - edges
center_0 center_1 center_2 center_3 center_4 crossroad_2_0 crossroad_2_1 bog_and_ide_0 bog_and_ide_1 crossroad_4_0 crossroad_14_0 nails_gallery_0 bella_donna_0 virtual  - people
to from - modes
)

(:init
(= (road_cost) 0)(mode from)(to-mode to)(from-mode from)(available virtual)(last-agent virtual)
(first-agent center_0)
(= (counter exit_b-crossroad_1) 0)
(= (counter center-crossroad_2) 0)
(= (counter center-crossroad_3) 0)
(= (counter center-crossroad_5) 0)
(= (counter center-crossroad_8) 0)
(= (counter center-crossroad_7) 0)
(= (counter exit_a-crossroad_4) 0)
(= (counter exit_a-crossroad_6) 0)
(= (counter crossroad_1-exit_b) 0)
(= (counter crossroad_1-crossroad_4) 0)
(= (counter crossroad_1-crossroad_2) 0)
(= (counter crossroad_2-crossroad_1) 0)
(= (counter crossroad_2-center) 0)
(= (counter crossroad_2-toilets) 0)
(= (counter bog_and_ide-crossroad_3) 0)
(= (counter crossroad_3-center) 0)
(= (counter crossroad_3-bog_and_ide) 0)
(= (counter crossroad_3-crossroad_4) 0)
(= (counter crossroad_4-crossroad_1) 0)
(= (counter crossroad_4-crossroad_3) 0)
(= (counter crossroad_4-exit_a) 0)
(= (counter crossroad_5-center) 0)
(= (counter crossroad_5-crossroad_6) 0)
(= (counter crossroad_6-crossroad_5) 0)
(= (counter crossroad_6-crossroad_13) 0)
(= (counter crossroad_6-exit_a) 0)
(= (counter crossroad_7-center) 0)
(= (counter crossroad_7-crossroad_17) 0)
(= (counter crossroad_8-center) 0)
(= (counter crossroad_8-crossroad_14) 0)
(= (counter toilets-crossroad_2) 0)
(= (counter crossroad_13-crossroad_6) 0)
(= (counter crossroad_13-smart_eyes) 0)
(= (counter crossroad_13-big_hall) 0)
(= (counter crossroad_14-crossroad_8) 0)
(= (counter crossroad_14-paw_sko) 0)
(= (counter crossroad_14-crossroad_15) 0)
(= (counter crossroad_15-crossroad_14) 0)
(= (counter crossroad_15-nails_gallery) 0)
(= (counter crossroad_15-bella_donna) 0)
(= (counter crossroad_15-crossroad_16) 0)
(= (counter paw_sko-crossroad_14) 0)
(= (counter smart_eyes-crossroad_13) 0)
(= (counter exit_c-crossroad_16) 0)
(= (counter nails_gallery-crossroad_15) 0)
(= (counter bella_donna-crossroad_15) 0)
(= (counter crossroad_16-crossroad_15) 0)
(= (counter crossroad_16-exit_c) 0)
(= (counter big_hall-crossroad_13) 0)
(= (counter big_hall-exit_d) 0)
(= (counter big_hall-crossroad_18) 0)
(= (counter crossroad_17-crossroad_7) 0)
(= (counter crossroad_17-crossroad_18) 0)
(= (counter crossroad_17-change) 0)
(= (counter exit_d-big_hall) 0)
(= (counter crossroad_18-big_hall) 0)
(= (counter crossroad_18-crossroad_17) 0)
(= (counter crossroad_18-synoptik) 0)
(= (counter synoptik-crossroad_18) 0)
(= (counter change-crossroad_17) 0)
(= (counter exit_b-exit_b) 0)
(= (counter center-center) 0)
(= (counter exit_a-exit_a) 0)
(= (counter crossroad_1-crossroad_1) 0)
(= (counter crossroad_2-crossroad_2) 0)
(= (counter bog_and_ide-bog_and_ide) 0)
(= (counter crossroad_3-crossroad_3) 0)
(= (counter crossroad_4-crossroad_4) 0)
(= (counter crossroad_5-crossroad_5) 0)
(= (counter crossroad_6-crossroad_6) 0)
(= (counter crossroad_7-crossroad_7) 0)
(= (counter crossroad_8-crossroad_8) 0)
(= (counter toilets-toilets) 0)
(= (counter crossroad_13-crossroad_13) 0)
(= (counter crossroad_14-crossroad_14) 0)
(= (counter crossroad_15-crossroad_15) 0)
(= (counter paw_sko-paw_sko) 0)
(= (counter smart_eyes-smart_eyes) 0)
(= (counter exit_c-exit_c) 0)
(= (counter nails_gallery-nails_gallery) 0)
(= (counter bella_donna-bella_donna) 0)
(= (counter crossroad_16-crossroad_16) 0)
(= (counter big_hall-big_hall) 0)
(= (counter crossroad_17-crossroad_17) 0)
(= (counter exit_d-exit_d) 0)
(= (counter crossroad_18-crossroad_18) 0)
(= (counter synoptik-synoptik) 0)
(= (counter change-change) 0)

(next-agent center_0 center_1)
(next-agent center_1 center_2)
(next-agent center_2 center_3)
(next-agent center_3 center_4)
(next-agent center_4 crossroad_2_0)
(next-agent crossroad_2_0 crossroad_2_1)
(next-agent crossroad_2_1 bog_and_ide_0)
(next-agent bog_and_ide_0 bog_and_ide_1)
(next-agent bog_and_ide_1 crossroad_4_0)
(next-agent crossroad_4_0 crossroad_14_0)
(next-agent crossroad_14_0 nails_gallery_0)
(next-agent nails_gallery_0 bella_donna_0)
(next-agent bella_donna_0 virtual)
(entry exit_b exit_b-exit_b)(leave exit_b-exit_b exit_b)
(entry center center-center)(leave center-center center)
(entry exit_a exit_a-exit_a)(leave exit_a-exit_a exit_a)
(entry crossroad_1 crossroad_1-crossroad_1)(leave crossroad_1-crossroad_1 crossroad_1)
(entry crossroad_2 crossroad_2-crossroad_2)(leave crossroad_2-crossroad_2 crossroad_2)
(entry bog_and_ide bog_and_ide-bog_and_ide)(leave bog_and_ide-bog_and_ide bog_and_ide)
(entry crossroad_3 crossroad_3-crossroad_3)(leave crossroad_3-crossroad_3 crossroad_3)
(entry crossroad_4 crossroad_4-crossroad_4)(leave crossroad_4-crossroad_4 crossroad_4)
(entry crossroad_5 crossroad_5-crossroad_5)(leave crossroad_5-crossroad_5 crossroad_5)
(entry crossroad_6 crossroad_6-crossroad_6)(leave crossroad_6-crossroad_6 crossroad_6)
(entry crossroad_7 crossroad_7-crossroad_7)(leave crossroad_7-crossroad_7 crossroad_7)
(entry crossroad_8 crossroad_8-crossroad_8)(leave crossroad_8-crossroad_8 crossroad_8)
(entry toilets toilets-toilets)(leave toilets-toilets toilets)
(entry crossroad_13 crossroad_13-crossroad_13)(leave crossroad_13-crossroad_13 crossroad_13)
(entry crossroad_14 crossroad_14-crossroad_14)(leave crossroad_14-crossroad_14 crossroad_14)
(entry crossroad_15 crossroad_15-crossroad_15)(leave crossroad_15-crossroad_15 crossroad_15)
(entry paw_sko paw_sko-paw_sko)(leave paw_sko-paw_sko paw_sko)
(entry smart_eyes smart_eyes-smart_eyes)(leave smart_eyes-smart_eyes smart_eyes)
(entry exit_c exit_c-exit_c)(leave exit_c-exit_c exit_c)
(entry nails_gallery nails_gallery-nails_gallery)(leave nails_gallery-nails_gallery nails_gallery)
(entry bella_donna bella_donna-bella_donna)(leave bella_donna-bella_donna bella_donna)
(entry crossroad_16 crossroad_16-crossroad_16)(leave crossroad_16-crossroad_16 crossroad_16)
(entry big_hall big_hall-big_hall)(leave big_hall-big_hall big_hall)
(entry crossroad_17 crossroad_17-crossroad_17)(leave crossroad_17-crossroad_17 crossroad_17)
(entry exit_d exit_d-exit_d)(leave exit_d-exit_d exit_d)
(entry crossroad_18 crossroad_18-crossroad_18)(leave crossroad_18-crossroad_18 crossroad_18)
(entry synoptik synoptik-synoptik)(leave synoptik-synoptik synoptik)
(entry change change-change)(leave change-change change)
(entry exit_b exit_b-crossroad_1)(leave exit_b-crossroad_1 crossroad_1)
(entry center center-crossroad_2)(leave center-crossroad_2 crossroad_2)
(entry center center-crossroad_3)(leave center-crossroad_3 crossroad_3)
(entry center center-crossroad_5)(leave center-crossroad_5 crossroad_5)
(entry center center-crossroad_8)(leave center-crossroad_8 crossroad_8)
(entry center center-crossroad_7)(leave center-crossroad_7 crossroad_7)
(entry exit_a exit_a-crossroad_4)(leave exit_a-crossroad_4 crossroad_4)
(entry exit_a exit_a-crossroad_6)(leave exit_a-crossroad_6 crossroad_6)
(entry crossroad_1 crossroad_1-exit_b)(leave crossroad_1-exit_b exit_b)
(entry crossroad_1 crossroad_1-crossroad_4)(leave crossroad_1-crossroad_4 crossroad_4)
(entry crossroad_1 crossroad_1-crossroad_2)(leave crossroad_1-crossroad_2 crossroad_2)
(entry crossroad_2 crossroad_2-crossroad_1)(leave crossroad_2-crossroad_1 crossroad_1)
(entry crossroad_2 crossroad_2-center)(leave crossroad_2-center center)
(entry crossroad_2 crossroad_2-toilets)(leave crossroad_2-toilets toilets)
(entry bog_and_ide bog_and_ide-crossroad_3)(leave bog_and_ide-crossroad_3 crossroad_3)
(entry crossroad_3 crossroad_3-center)(leave crossroad_3-center center)
(entry crossroad_3 crossroad_3-bog_and_ide)(leave crossroad_3-bog_and_ide bog_and_ide)
(entry crossroad_3 crossroad_3-crossroad_4)(leave crossroad_3-crossroad_4 crossroad_4)
(entry crossroad_4 crossroad_4-crossroad_1)(leave crossroad_4-crossroad_1 crossroad_1)
(entry crossroad_4 crossroad_4-crossroad_3)(leave crossroad_4-crossroad_3 crossroad_3)
(entry crossroad_4 crossroad_4-exit_a)(leave crossroad_4-exit_a exit_a)
(entry crossroad_5 crossroad_5-center)(leave crossroad_5-center center)
(entry crossroad_5 crossroad_5-crossroad_6)(leave crossroad_5-crossroad_6 crossroad_6)
(entry crossroad_6 crossroad_6-crossroad_5)(leave crossroad_6-crossroad_5 crossroad_5)
(entry crossroad_6 crossroad_6-crossroad_13)(leave crossroad_6-crossroad_13 crossroad_13)
(entry crossroad_6 crossroad_6-exit_a)(leave crossroad_6-exit_a exit_a)
(entry crossroad_7 crossroad_7-center)(leave crossroad_7-center center)
(entry crossroad_7 crossroad_7-crossroad_17)(leave crossroad_7-crossroad_17 crossroad_17)
(entry crossroad_8 crossroad_8-center)(leave crossroad_8-center center)
(entry crossroad_8 crossroad_8-crossroad_14)(leave crossroad_8-crossroad_14 crossroad_14)
(entry toilets toilets-crossroad_2)(leave toilets-crossroad_2 crossroad_2)
(entry crossroad_13 crossroad_13-crossroad_6)(leave crossroad_13-crossroad_6 crossroad_6)
(entry crossroad_13 crossroad_13-smart_eyes)(leave crossroad_13-smart_eyes smart_eyes)
(entry crossroad_13 crossroad_13-big_hall)(leave crossroad_13-big_hall big_hall)
(entry crossroad_14 crossroad_14-crossroad_8)(leave crossroad_14-crossroad_8 crossroad_8)
(entry crossroad_14 crossroad_14-paw_sko)(leave crossroad_14-paw_sko paw_sko)
(entry crossroad_14 crossroad_14-crossroad_15)(leave crossroad_14-crossroad_15 crossroad_15)
(entry crossroad_15 crossroad_15-crossroad_14)(leave crossroad_15-crossroad_14 crossroad_14)
(entry crossroad_15 crossroad_15-nails_gallery)(leave crossroad_15-nails_gallery nails_gallery)
(entry crossroad_15 crossroad_15-bella_donna)(leave crossroad_15-bella_donna bella_donna)
(entry crossroad_15 crossroad_15-crossroad_16)(leave crossroad_15-crossroad_16 crossroad_16)
(entry paw_sko paw_sko-crossroad_14)(leave paw_sko-crossroad_14 crossroad_14)
(entry smart_eyes smart_eyes-crossroad_13)(leave smart_eyes-crossroad_13 crossroad_13)
(entry exit_c exit_c-crossroad_16)(leave exit_c-crossroad_16 crossroad_16)
(entry nails_gallery nails_gallery-crossroad_15)(leave nails_gallery-crossroad_15 crossroad_15)
(entry bella_donna bella_donna-crossroad_15)(leave bella_donna-crossroad_15 crossroad_15)
(entry crossroad_16 crossroad_16-crossroad_15)(leave crossroad_16-crossroad_15 crossroad_15)
(entry crossroad_16 crossroad_16-exit_c)(leave crossroad_16-exit_c exit_c)
(entry big_hall big_hall-crossroad_13)(leave big_hall-crossroad_13 crossroad_13)
(entry big_hall big_hall-exit_d)(leave big_hall-exit_d exit_d)
(entry big_hall big_hall-crossroad_18)(leave big_hall-crossroad_18 crossroad_18)
(entry crossroad_17 crossroad_17-crossroad_7)(leave crossroad_17-crossroad_7 crossroad_7)
(entry crossroad_17 crossroad_17-crossroad_18)(leave crossroad_17-crossroad_18 crossroad_18)
(entry crossroad_17 crossroad_17-change)(leave crossroad_17-change change)
(entry exit_d exit_d-big_hall)(leave exit_d-big_hall big_hall)
(entry crossroad_18 crossroad_18-big_hall)(leave crossroad_18-big_hall big_hall)
(entry crossroad_18 crossroad_18-crossroad_17)(leave crossroad_18-crossroad_17 crossroad_17)
(entry crossroad_18 crossroad_18-synoptik)(leave crossroad_18-synoptik synoptik)
(entry synoptik synoptik-crossroad_18)(leave synoptik-crossroad_18 crossroad_18)
(entry change change-crossroad_17)(leave change-crossroad_17 crossroad_17)
(= (road_risk exit_b-crossroad_1) 1)
(= (capacity-0 exit_b-crossroad_1) 80)(= (crowding-0 exit_b-crossroad_1) 1)
(= (capacity-1 exit_b-crossroad_1) 100)(= (crowding-1 exit_b-crossroad_1) 50)
(= (capacity-2 exit_b-crossroad_1) 200)(= (crowding-2 exit_b-crossroad_1) 100)
(= (capacity-3 exit_b-crossroad_1) 200)(= (crowding-3 exit_b-crossroad_1) 100)
(= (capacity-4 exit_b-crossroad_1) 200)(= (crowding-4 exit_b-crossroad_1) 100)
(= (capacity-5 exit_b-crossroad_1) 200)(= (crowding-5 exit_b-crossroad_1) 100)
(= (capacity-6 exit_b-crossroad_1) 200)(= (crowding-6 exit_b-crossroad_1) 100)
(= (capacity-7 exit_b-crossroad_1) 200)(= (crowding-7 exit_b-crossroad_1) 100)
(= (capacity-8 exit_b-crossroad_1) 200)(= (crowding-8 exit_b-crossroad_1) 100)
(= (capacity-9 exit_b-crossroad_1) 200)(= (crowding-9 exit_b-crossroad_1) 100)
(= (road_risk center-crossroad_2) 1)
(= (capacity-0 center-crossroad_2) 99999)(= (crowding-0 center-crossroad_2) 1)
(= (road_risk center-crossroad_3) 1)
(= (capacity-0 center-crossroad_3) 99999)(= (crowding-0 center-crossroad_3) 1)
(= (road_risk center-crossroad_5) 1)
(= (capacity-0 center-crossroad_5) 99999)(= (crowding-0 center-crossroad_5) 1)
(= (road_risk center-crossroad_8) 1)
(= (capacity-0 center-crossroad_8) 99999)(= (crowding-0 center-crossroad_8) 1)
(= (road_risk center-crossroad_7) 1)
(= (capacity-0 center-crossroad_7) 99999)(= (crowding-0 center-crossroad_7) 1)
(= (road_risk exit_a-crossroad_4) 1)
(= (capacity-0 exit_a-crossroad_4) 99999)(= (crowding-0 exit_a-crossroad_4) 1)
(= (road_risk exit_a-crossroad_6) 1)
(= (capacity-0 exit_a-crossroad_6) 99999)(= (crowding-0 exit_a-crossroad_6) 1)
(= (road_risk crossroad_1-exit_b) 1)
(= (capacity-0 crossroad_1-exit_b) 80)(= (crowding-0 crossroad_1-exit_b) 1)
(= (capacity-1 crossroad_1-exit_b) 100)(= (crowding-1 crossroad_1-exit_b) 50)
(= (capacity-2 crossroad_1-exit_b) 200)(= (crowding-2 crossroad_1-exit_b) 100)
(= (capacity-3 crossroad_1-exit_b) 200)(= (crowding-3 crossroad_1-exit_b) 100)
(= (capacity-4 crossroad_1-exit_b) 200)(= (crowding-4 crossroad_1-exit_b) 100)
(= (capacity-5 crossroad_1-exit_b) 200)(= (crowding-5 crossroad_1-exit_b) 100)
(= (capacity-6 crossroad_1-exit_b) 200)(= (crowding-6 crossroad_1-exit_b) 100)
(= (capacity-7 crossroad_1-exit_b) 200)(= (crowding-7 crossroad_1-exit_b) 100)
(= (capacity-8 crossroad_1-exit_b) 200)(= (crowding-8 crossroad_1-exit_b) 100)
(= (capacity-9 crossroad_1-exit_b) 200)(= (crowding-9 crossroad_1-exit_b) 100)
(= (road_risk crossroad_1-crossroad_4) 100)
(= (capacity-0 crossroad_1-crossroad_4) 100)(= (crowding-0 crossroad_1-crossroad_4) 1)
(= (capacity-1 crossroad_1-crossroad_4) 200)(= (crowding-1 crossroad_1-crossroad_4) 20)
(= (capacity-2 crossroad_1-crossroad_4) 400)(= (crowding-2 crossroad_1-crossroad_4) 60)
(= (capacity-3 crossroad_1-crossroad_4) 600)(= (crowding-3 crossroad_1-crossroad_4) 100)
(= (capacity-4 crossroad_1-crossroad_4) 600)(= (crowding-4 crossroad_1-crossroad_4) 100)
(= (capacity-5 crossroad_1-crossroad_4) 600)(= (crowding-5 crossroad_1-crossroad_4) 100)
(= (capacity-6 crossroad_1-crossroad_4) 600)(= (crowding-6 crossroad_1-crossroad_4) 100)
(= (capacity-7 crossroad_1-crossroad_4) 600)(= (crowding-7 crossroad_1-crossroad_4) 100)
(= (capacity-8 crossroad_1-crossroad_4) 600)(= (crowding-8 crossroad_1-crossroad_4) 100)
(= (capacity-9 crossroad_1-crossroad_4) 600)(= (crowding-9 crossroad_1-crossroad_4) 100)
(= (road_risk crossroad_1-crossroad_2) 1)
(= (capacity-0 crossroad_1-crossroad_2) 99999)(= (crowding-0 crossroad_1-crossroad_2) 1)
(= (road_risk crossroad_2-crossroad_1) 1)
(= (capacity-0 crossroad_2-crossroad_1) 99999)(= (crowding-0 crossroad_2-crossroad_1) 1)
(= (road_risk crossroad_2-center) 1)
(= (capacity-0 crossroad_2-center) 99999)(= (crowding-0 crossroad_2-center) 1)
(= (road_risk crossroad_2-toilets) 1)
(= (capacity-0 crossroad_2-toilets) 99999)(= (crowding-0 crossroad_2-toilets) 1)
(= (road_risk bog_and_ide-crossroad_3) 1)
(= (capacity-0 bog_and_ide-crossroad_3) 99999)(= (crowding-0 bog_and_ide-crossroad_3) 1)
(= (road_risk crossroad_3-center) 1)
(= (capacity-0 crossroad_3-center) 99999)(= (crowding-0 crossroad_3-center) 1)
(= (road_risk crossroad_3-bog_and_ide) 1)
(= (capacity-0 crossroad_3-bog_and_ide) 99999)(= (crowding-0 crossroad_3-bog_and_ide) 1)
(= (road_risk crossroad_3-crossroad_4) 100)
(= (capacity-0 crossroad_3-crossroad_4) 99999)(= (crowding-0 crossroad_3-crossroad_4) 1)
(= (road_risk crossroad_4-crossroad_1) 100)
(= (capacity-0 crossroad_4-crossroad_1) 100)(= (crowding-0 crossroad_4-crossroad_1) 1)
(= (capacity-1 crossroad_4-crossroad_1) 200)(= (crowding-1 crossroad_4-crossroad_1) 20)
(= (capacity-2 crossroad_4-crossroad_1) 400)(= (crowding-2 crossroad_4-crossroad_1) 60)
(= (capacity-3 crossroad_4-crossroad_1) 600)(= (crowding-3 crossroad_4-crossroad_1) 100)
(= (capacity-4 crossroad_4-crossroad_1) 600)(= (crowding-4 crossroad_4-crossroad_1) 100)
(= (capacity-5 crossroad_4-crossroad_1) 600)(= (crowding-5 crossroad_4-crossroad_1) 100)
(= (capacity-6 crossroad_4-crossroad_1) 600)(= (crowding-6 crossroad_4-crossroad_1) 100)
(= (capacity-7 crossroad_4-crossroad_1) 600)(= (crowding-7 crossroad_4-crossroad_1) 100)
(= (capacity-8 crossroad_4-crossroad_1) 600)(= (crowding-8 crossroad_4-crossroad_1) 100)
(= (capacity-9 crossroad_4-crossroad_1) 600)(= (crowding-9 crossroad_4-crossroad_1) 100)
(= (road_risk crossroad_4-crossroad_3) 100)
(= (capacity-0 crossroad_4-crossroad_3) 99999)(= (crowding-0 crossroad_4-crossroad_3) 1)
(= (road_risk crossroad_4-exit_a) 1)
(= (capacity-0 crossroad_4-exit_a) 99999)(= (crowding-0 crossroad_4-exit_a) 1)
(= (road_risk crossroad_5-center) 1)
(= (capacity-0 crossroad_5-center) 99999)(= (crowding-0 crossroad_5-center) 1)
(= (road_risk crossroad_5-crossroad_6) 80)
(= (capacity-0 crossroad_5-crossroad_6) 100)(= (crowding-0 crossroad_5-crossroad_6) 1)
(= (capacity-1 crossroad_5-crossroad_6) 200)(= (crowding-1 crossroad_5-crossroad_6) 20)
(= (capacity-2 crossroad_5-crossroad_6) 400)(= (crowding-2 crossroad_5-crossroad_6) 60)
(= (capacity-3 crossroad_5-crossroad_6) 600)(= (crowding-3 crossroad_5-crossroad_6) 100)
(= (capacity-4 crossroad_5-crossroad_6) 600)(= (crowding-4 crossroad_5-crossroad_6) 100)
(= (capacity-5 crossroad_5-crossroad_6) 600)(= (crowding-5 crossroad_5-crossroad_6) 100)
(= (capacity-6 crossroad_5-crossroad_6) 600)(= (crowding-6 crossroad_5-crossroad_6) 100)
(= (capacity-7 crossroad_5-crossroad_6) 600)(= (crowding-7 crossroad_5-crossroad_6) 100)
(= (capacity-8 crossroad_5-crossroad_6) 600)(= (crowding-8 crossroad_5-crossroad_6) 100)
(= (capacity-9 crossroad_5-crossroad_6) 600)(= (crowding-9 crossroad_5-crossroad_6) 100)
(= (road_risk crossroad_6-crossroad_5) 80)
(= (capacity-0 crossroad_6-crossroad_5) 100)(= (crowding-0 crossroad_6-crossroad_5) 1)
(= (capacity-1 crossroad_6-crossroad_5) 200)(= (crowding-1 crossroad_6-crossroad_5) 20)
(= (capacity-2 crossroad_6-crossroad_5) 400)(= (crowding-2 crossroad_6-crossroad_5) 60)
(= (capacity-3 crossroad_6-crossroad_5) 600)(= (crowding-3 crossroad_6-crossroad_5) 100)
(= (capacity-4 crossroad_6-crossroad_5) 600)(= (crowding-4 crossroad_6-crossroad_5) 100)
(= (capacity-5 crossroad_6-crossroad_5) 600)(= (crowding-5 crossroad_6-crossroad_5) 100)
(= (capacity-6 crossroad_6-crossroad_5) 600)(= (crowding-6 crossroad_6-crossroad_5) 100)
(= (capacity-7 crossroad_6-crossroad_5) 600)(= (crowding-7 crossroad_6-crossroad_5) 100)
(= (capacity-8 crossroad_6-crossroad_5) 600)(= (crowding-8 crossroad_6-crossroad_5) 100)
(= (capacity-9 crossroad_6-crossroad_5) 600)(= (crowding-9 crossroad_6-crossroad_5) 100)
(= (road_risk crossroad_6-crossroad_13) 1)
(= (capacity-0 crossroad_6-crossroad_13) 99999)(= (crowding-0 crossroad_6-crossroad_13) 1)
(= (road_risk crossroad_6-exit_a) 1)
(= (capacity-0 crossroad_6-exit_a) 99999)(= (crowding-0 crossroad_6-exit_a) 1)
(= (road_risk crossroad_7-center) 1)
(= (capacity-0 crossroad_7-center) 99999)(= (crowding-0 crossroad_7-center) 1)
(= (road_risk crossroad_7-crossroad_17) 1)
(= (capacity-0 crossroad_7-crossroad_17) 99999)(= (crowding-0 crossroad_7-crossroad_17) 1)
(= (road_risk crossroad_8-center) 1)
(= (capacity-0 crossroad_8-center) 99999)(= (crowding-0 crossroad_8-center) 1)
(= (road_risk crossroad_8-crossroad_14) 1)
(= (capacity-0 crossroad_8-crossroad_14) 99999)(= (crowding-0 crossroad_8-crossroad_14) 1)
(= (road_risk toilets-crossroad_2) 1)
(= (capacity-0 toilets-crossroad_2) 99999)(= (crowding-0 toilets-crossroad_2) 1)
(= (road_risk crossroad_13-crossroad_6) 1)
(= (capacity-0 crossroad_13-crossroad_6) 99999)(= (crowding-0 crossroad_13-crossroad_6) 1)
(= (road_risk crossroad_13-smart_eyes) 1)
(= (capacity-0 crossroad_13-smart_eyes) 99999)(= (crowding-0 crossroad_13-smart_eyes) 1)
(= (road_risk crossroad_13-big_hall) 1)
(= (capacity-0 crossroad_13-big_hall) 99999)(= (crowding-0 crossroad_13-big_hall) 1)
(= (road_risk crossroad_14-crossroad_8) 1)
(= (capacity-0 crossroad_14-crossroad_8) 99999)(= (crowding-0 crossroad_14-crossroad_8) 1)
(= (road_risk crossroad_14-paw_sko) 1)
(= (capacity-0 crossroad_14-paw_sko) 99999)(= (crowding-0 crossroad_14-paw_sko) 1)
(= (road_risk crossroad_14-crossroad_15) 1)
(= (capacity-0 crossroad_14-crossroad_15) 99999)(= (crowding-0 crossroad_14-crossroad_15) 1)
(= (road_risk crossroad_15-crossroad_14) 1)
(= (capacity-0 crossroad_15-crossroad_14) 99999)(= (crowding-0 crossroad_15-crossroad_14) 1)
(= (road_risk crossroad_15-nails_gallery) 1)
(= (capacity-0 crossroad_15-nails_gallery) 99999)(= (crowding-0 crossroad_15-nails_gallery) 1)
(= (road_risk crossroad_15-bella_donna) 1)
(= (capacity-0 crossroad_15-bella_donna) 99999)(= (crowding-0 crossroad_15-bella_donna) 1)
(= (road_risk crossroad_15-crossroad_16) 1)
(= (capacity-0 crossroad_15-crossroad_16) 99999)(= (crowding-0 crossroad_15-crossroad_16) 1)
(= (road_risk paw_sko-crossroad_14) 1)
(= (capacity-0 paw_sko-crossroad_14) 99999)(= (crowding-0 paw_sko-crossroad_14) 1)
(= (road_risk smart_eyes-crossroad_13) 1)
(= (capacity-0 smart_eyes-crossroad_13) 99999)(= (crowding-0 smart_eyes-crossroad_13) 1)
(= (road_risk exit_c-crossroad_16) 1)
(= (capacity-0 exit_c-crossroad_16) 99999)(= (crowding-0 exit_c-crossroad_16) 1)
(= (road_risk nails_gallery-crossroad_15) 1)
(= (capacity-0 nails_gallery-crossroad_15) 99999)(= (crowding-0 nails_gallery-crossroad_15) 1)
(= (road_risk bella_donna-crossroad_15) 1)
(= (capacity-0 bella_donna-crossroad_15) 99999)(= (crowding-0 bella_donna-crossroad_15) 1)
(= (road_risk crossroad_16-crossroad_15) 1)
(= (capacity-0 crossroad_16-crossroad_15) 99999)(= (crowding-0 crossroad_16-crossroad_15) 1)
(= (road_risk crossroad_16-exit_c) 1)
(= (capacity-0 crossroad_16-exit_c) 99999)(= (crowding-0 crossroad_16-exit_c) 1)
(= (road_risk big_hall-crossroad_13) 1)
(= (capacity-0 big_hall-crossroad_13) 99999)(= (crowding-0 big_hall-crossroad_13) 1)
(= (road_risk big_hall-exit_d) 1)
(= (capacity-0 big_hall-exit_d) 99999)(= (crowding-0 big_hall-exit_d) 1)
(= (road_risk big_hall-crossroad_18) 1)
(= (capacity-0 big_hall-crossroad_18) 99999)(= (crowding-0 big_hall-crossroad_18) 1)
(= (road_risk crossroad_17-crossroad_7) 1)
(= (capacity-0 crossroad_17-crossroad_7) 99999)(= (crowding-0 crossroad_17-crossroad_7) 1)
(= (road_risk crossroad_17-crossroad_18) 1)
(= (capacity-0 crossroad_17-crossroad_18) 99999)(= (crowding-0 crossroad_17-crossroad_18) 1)
(= (road_risk crossroad_17-change) 1)
(= (capacity-0 crossroad_17-change) 99999)(= (crowding-0 crossroad_17-change) 1)
(= (road_risk exit_d-big_hall) 1)
(= (capacity-0 exit_d-big_hall) 99999)(= (crowding-0 exit_d-big_hall) 1)
(= (road_risk crossroad_18-big_hall) 1)
(= (capacity-0 crossroad_18-big_hall) 99999)(= (crowding-0 crossroad_18-big_hall) 1)
(= (road_risk crossroad_18-crossroad_17) 1)
(= (capacity-0 crossroad_18-crossroad_17) 99999)(= (crowding-0 crossroad_18-crossroad_17) 1)
(= (road_risk crossroad_18-synoptik) 1)
(= (capacity-0 crossroad_18-synoptik) 99999)(= (crowding-0 crossroad_18-synoptik) 1)
(= (road_risk synoptik-crossroad_18) 1)
(= (capacity-0 synoptik-crossroad_18) 99999)(= (crowding-0 synoptik-crossroad_18) 1)
(= (road_risk change-crossroad_17) 1)
(= (capacity-0 change-crossroad_17) 99999)(= (crowding-0 change-crossroad_17) 1)
(= (road_risk exit_b-exit_b) 1)
(= (road_risk center-center) 1)
(= (road_risk exit_a-exit_a) 1)
(= (road_risk crossroad_1-crossroad_1) 1)
(= (road_risk crossroad_2-crossroad_2) 1)
(= (road_risk bog_and_ide-bog_and_ide) 1)
(= (road_risk crossroad_3-crossroad_3) 1)
(= (road_risk crossroad_4-crossroad_4) 1)
(= (road_risk crossroad_5-crossroad_5) 1)
(= (road_risk crossroad_6-crossroad_6) 1)
(= (road_risk crossroad_7-crossroad_7) 1)
(= (road_risk crossroad_8-crossroad_8) 1)
(= (road_risk toilets-toilets) 1)
(= (road_risk crossroad_13-crossroad_13) 1)
(= (road_risk crossroad_14-crossroad_14) 1)
(= (road_risk crossroad_15-crossroad_15) 1)
(= (road_risk paw_sko-paw_sko) 1)
(= (road_risk smart_eyes-smart_eyes) 1)
(= (road_risk exit_c-exit_c) 1)
(= (road_risk nails_gallery-nails_gallery) 1)
(= (road_risk bella_donna-bella_donna) 1)
(= (road_risk crossroad_16-crossroad_16) 1)
(= (road_risk big_hall-big_hall) 1)
(= (road_risk crossroad_17-crossroad_17) 1)
(= (road_risk exit_d-exit_d) 1)
(= (road_risk crossroad_18-crossroad_18) 1)
(= (road_risk synoptik-synoptik) 1)
(= (road_risk change-change) 1)
(at_node center_0 center)
(at_node center_1 center)
(at_node center_2 center)
(at_node center_3 center)
(at_node center_4 center)
(at_node crossroad_2_0 crossroad_2)
(at_node crossroad_2_1 crossroad_2)
(at_node bog_and_ide_0 bog_and_ide)
(at_node bog_and_ide_1 bog_and_ide)
(at_node crossroad_4_0 crossroad_4)
(at_node crossroad_14_0 crossroad_14)
(at_node nails_gallery_0 nails_gallery)
(at_node bella_donna_0 bella_donna)
(exit exit_b)
(exit exit_a)
(exit exit_c)
(exit exit_d)
)

(:goal (and
(at-exit center_0)
(at-exit center_1)
(at-exit center_2)
(at-exit center_3)
(at-exit center_4)
(at-exit crossroad_2_0)
(at-exit crossroad_2_1)
(at-exit bog_and_ide_0)
(at-exit bog_and_ide_1)
(at-exit crossroad_4_0)
(at-exit crossroad_14_0)
(at-exit nails_gallery_0)
(at-exit bella_donna_0)
(forall (?e - edges) (= (counter ?e) 0))))

(:metric minimize (road_cost)))