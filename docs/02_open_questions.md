# Open Questions

## Q1. What is the minimal state variable for LCST collapse?

候选：

* polymer volume fraction;
* swelling ratio;
* porosity;
* permeability;
* scalar collapsed fraction.

## Q2. How should transport degradation be modeled?

候选：

* concentration diffusivity decreases with collapse;
* reaction accessibility decreases with collapse;
* heat diffusivity changes with collapse;
* permeability changes with poroelastic state.

## Q3. Is a well-mixed ODE model incapable of oscillating?

需要比较 homogeneous ODE 与 spatial PDE。

## Q4. Does the mechanism require a moving front?

需要定义 front observable。

## Q5. What distinguishes this from thermal runaway with recovery?

需要证明 closed relaxation cycle 和吸引子结构。

## Q6. Is homogeneous linear stability insufficient?

需要解释：

* 均匀态线性稳定性只能描述局部小扰动；
* 空间 PDE 中 transport barrier 和 front dynamics 可能是非线性、有限幅度、空间局域结构；
* 需要通过 PDE simulation / reduced front model / phase-plane diagnostics 验证。

## Q7. What boundary conditions are physically relevant?

候选：

* fixed external reactant concentration;
* convective heat exchange;
* no-flux mechanical boundary;
* symmetry boundary.

## Q8. What are the minimal observables?

候选：

* maximum temperature;
* reaction rate;
* collapsed skin thickness;
* reactant penetration depth;
* front position;
* total heat release;
* oscillation period;
* phase lag between temperature, collapse, and reactant flux.

## Q9. Is the reaction strictly first-order?

初步推导正文使用 first-order reaction 和 `Rhat proportional to u`，但 appendix 保留 `u^n` 的一般形式。需要确认最终模型是否固定为 `n = 1`。

## Q10. Which notation is canonical?

需要统一：

* `mu` versus nondimensional `m`;
* `xi` versus `x`;
* compact equations中吸收了 `alpha`、`delta` 的 `D`、`K`，versus appendix 中显式保留 `alpha`、`delta` 的写法。

## Q11. What are the final material functions?

尚需定义或明确简化：

* `C(J)`;
* `K(J)`;
* `M(J, theta)`;
* `D(J, theta)`;
* mobility exponent `m_mob`;
* whether thermal conductivity or heat capacity changes during collapse.

## Q12. Are the boundary-condition signs consistent?

初步推导中 compact surface condition 和 full flux form 的 reactant Robin condition 使用了不同的外向通量写法。需要固定通量方向、符号约定和 `mu_b` / `m_b` convention。

## Q13. Are the asymptotic assumptions justified?

需要为以下近似给出物理范围或参数估计：

* `Pe_T << 1` for neglecting enthalpy advection;
* `epsilon_T << 1` for simplifying the Arrhenius factor;
* one-dimensional planar slab approximation.

## Q14. What is the exact homogeneous ODE limit?

目前初步推导给出 homogeneous steady-state balances 和 `k = 0` linear matrix，但尚未完整写出 homogeneous ODE dynamical system。需要明确 well-mixed ODE 是否能或不能振荡。

## Q15. Which source-appendix numerical claims must be reproduced?

Appendix 包含 spinodal-decomposition numerical verification notes。当前 repo 只记录这些内容，尚未复现。需要决定哪些数值 claim 属于后续 verification task。
