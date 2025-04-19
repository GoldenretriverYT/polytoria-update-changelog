# Changes
## EnvironmentProxy
Inherits from: [InstanceProxy](#InstanceProxy)
- Method `RebuildNavMesh` changed parameters: 
  - Parameter `root` added
## MeshPartProxy
Inherits from: [PartProxy](#PartProxy)
- Method `PlayAnimation` changed parameters: 
  - Parameter `objectPath` added
  - Parameter `speed` added
  - Parameter `loop` added
- Method `StopAnimation` changed parameters: 
  - Parameter `name` added
- New method added: `GetAnimationSources`
- New method added: `GetAnimationInfo`
- New property added: `PlayAnimationOnStart` of type ``System.Boolean``
- New property added: `CollisionType` of type ``Polytoria.Datamodel.CollisionType``
## NPCProxy
Inherits from: [DynamicInstanceProxy](#DynamicInstanceProxy)
- New method added: `EquipTool`
- New method added: `DropTool`
## UIImageProxy
Inherits from: [UIFieldProxy](#UIFieldProxy)
- New property added: `Clickable` of type ``System.Boolean``
