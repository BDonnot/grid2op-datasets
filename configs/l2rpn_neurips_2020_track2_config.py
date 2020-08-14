from grid2op.Action import TopologyAndDispatchAction
from grid2op.Reward import RedispReward
from grid2op.Rules import DefaultRules
from grid2op.Chronics import Multifolder
from grid2op.Chronics import GridStateFromFileWithForecastsWithMaintenance
from grid2op.Backend import PandaPowerBackend

config = {
    "backend": PandaPowerBackend,
    "action_class": TopologyAndDispatchAction,
    "observation_class": None,
    "reward_class": RedispReward,
    "gamerules_class": DefaultRules,
    "chronics_class": Multifolder,
    "grid_value_class": GridStateFromFileWithForecastsWithMaintenance,
    "volagecontroler_class": None,
    "names_chronics_to_grid": None,
    "thermal_limits": [233.4, 354.4, 566.2, 314.4, 336.6, 318.4, 8., 480.,
                       436.5, 681.8, 357.6, 336.9, 682.5, 419.2, 289.7, 626.2,
                       256.1, 147.1, 69.1, 165.9, 1261.5, 1105.5, 329.4, 427.1,
                       224.2, 267.4, 285.6, 429.8, 253.1, 479.6, 238.3, 452.6,
                       312.9, 627.8, 196.1, 328.1, 317.1, 180.6, 293.8, 151.,
                       565.5, 309.8, 475.9, 208.6, 646.9, 616.9, 364.1, 523.9,
                       191.7, 866.2, 583.1, 569.6, 472.1, 516.8, 292.9, 282.4,
                       246.9, 301.3, 766.9, 401.2, 306.9, 314.4, 333.4, 748.9,
                       513.4, 243.6, 513., 167.8, 175.2, 492., 420.4, 417.4,
                       199.3, 457.5, 160.5, 161., 176.4, 275.2, 153.2, 228.4,
                       210.8, 394.9, 371.4, 147.9, 602.2, 708.8, 120.6, 546.,
                       719.2, 258.4, 424.1, 180.6, 253.7, 314.4, 674.2, 972.,
                       569.6, 800.2, 316.9, 162.3, 397.8, 487.5, 490.9, 207.4,
                       590.6, 221.6, 186.4, 698.2, 208.1, 226.9, 60.9, 231.9,
                       272.6, 212.8, 749.2, 332.4, 348., 456., 362.1, 414.4,
                       310.1, 371.4, 401.2, 124.3, 298.5, 86.4, 213.9, 160.8,
                       112.2, 458.9, 291.4, 489., 489., 124.6, 196.7, 191.9,
                       238.4, 174.2, 105.6, 143.7, 393.6, 293.4, 288.9, 107.7,
                       415.5, 252.9, 124.2, 154.4, 85.9, 106.5, 142., 524.6,
                       124., 130.2, 86.2, 278.1, 182., 592.1, 173.1, 249.8,
                       441., 344.2, 609., 722.8, 494.6, 494.6, 196.7, 151.8,
                       263.4, 364.1, 327., 459., 336.6, 887.2, 615.2, 997.1,
                       68.2, 472.6, 546.6, 370.5, 441., 300.3, 656.2, 1035.4,
                       1246.5, 997.1]
}
