export class Controller {
  public buttons: number[] = new Array(16);
  public axes: number[] = new Array(4);
  public timestamp: number;
  private pre6: number = 0.5;
  private pre7: number = 0.5;

  constructor(controller: Gamepad) {
    this.writeController;
  }

  writeController(controller: Gamepad) {
    this.timestamp = controller.timestamp;

    if (controller.axes.length === 8) {
      this.ps4ToStandard(controller);
    } else if (controller.axes.length === 6) {
      this.oldPSToStandard(controller);
    } else if (
      controller.axes.length === 4 ||
      controller.mapping === 'standard'
    ) {
      this.commonToStandard(controller);
    } else {
      console.log('This controller does not seem to be supported.');
    }
  }

  updateController(controller: Gamepad) {
    this.timestamp = controller.timestamp;

    this.writeController(controller);
  }

  ps4ToStandard(controller: Gamepad) {
    if (this.pre6 && controller.axes[2] != 0) {
      this.pre6 = 0;
    }

    if (this.pre7 && controller.axes[5] != 0) {
      this.pre7 = 0;
    }

    this.buttons[0] = controller.buttons[0].value;
    this.buttons[1] = controller.buttons[1].value;
    this.buttons[2] = controller.buttons[3].value;
    this.buttons[3] = controller.buttons[2].value;
    this.buttons[4] = controller.buttons[4].value;
    this.buttons[5] = controller.buttons[5].value;
    this.buttons[6] = (controller.axes[2].valueOf() + 1) / 2 - this.pre6;
    this.buttons[7] = (controller.axes[5].valueOf() + 1) / 2 - this.pre7;
    if (controller.buttons.length < 12) {
      this.buttons[8] = controller.buttons[8].value;
      this.buttons[9] = controller.buttons[9].value;
      this.buttons[10] = controller.buttons[11].value;
      this.buttons[11] = controller.buttons[12].value;
      this.buttons[16] = controller.buttons[10].value;
    } else {
      this.buttons[8] = controller.buttons[6].value;
      this.buttons[9] = controller.buttons[7].value;
      this.buttons[10] = controller.buttons[9].value;
      this.buttons[11] = controller.buttons[10].value;
      this.buttons[16] = controller.buttons[18].value;
    }
    this.buttons[12] = Math.max(0, controller.axes[6].valueOf());
    this.buttons[13] = Math.max(0, -1 * controller.axes[6].valueOf());
    this.buttons[14] = Math.max(0, controller.axes[7].valueOf());
    this.buttons[15] = Math.max(0, -1 * controller.axes[7].valueOf());

    this.axes[0] = controller.axes[0].valueOf();
    this.axes[1] = controller.axes[1].valueOf();
    this.axes[2] = controller.axes[3].valueOf();
    this.axes[3] = controller.axes[4].valueOf();
  }

  oldPSToStandard(controller: Gamepad) {
    if (this.pre6 && controller.axes[2] != 0) {
      this.pre6 = 0;
    }

    if (this.pre7 && controller.axes[5] != 0) {
      this.pre7 = 0;
    }

    this.buttons[0] = controller.buttons[0].value;
    this.buttons[1] = controller.buttons[1].value;
    this.buttons[2] = controller.buttons[3].value;
    this.buttons[3] = controller.buttons[2].value;
    this.buttons[4] = controller.buttons[4].value;
    this.buttons[5] = controller.buttons[5].value;
    this.buttons[6] = (controller.axes[2].valueOf() + 1) / 2 - this.pre6;
    this.buttons[7] = (controller.axes[5].valueOf() + 1) / 2 - this.pre7;
    this.buttons[8] = controller.buttons[8].value;
    this.buttons[9] = controller.buttons[9].value;
    this.buttons[10] = controller.buttons[11].value;
    this.buttons[11] = controller.buttons[12].value;
    this.buttons[12] = controller.buttons[13].value;
    this.buttons[13] = controller.buttons[14].value;
    this.buttons[14] = controller.buttons[15].value;
    this.buttons[15] = controller.buttons[16].value;
    this.buttons[16] = controller.buttons[10].value;

    this.axes[0] = controller.axes[0].valueOf();
    this.axes[1] = controller.axes[1].valueOf();
    this.axes[2] = controller.axes[3].valueOf();
    this.axes[3] = controller.axes[4].valueOf();
  }

  commonToStandard(controller: Gamepad) {
    this.buttons[0] = controller.buttons[0].value;
    this.buttons[1] = controller.buttons[1].value;
    this.buttons[2] = controller.buttons[2].value;
    this.buttons[3] = controller.buttons[3].value;
    this.buttons[4] = controller.buttons[4].value;
    this.buttons[5] = controller.buttons[5].value;
    this.buttons[6] = controller.buttons[6].value;
    this.buttons[7] = controller.buttons[7].value;
    this.buttons[8] = controller.buttons[8].value;
    this.buttons[9] = controller.buttons[9].value;
    this.buttons[10] = controller.buttons[10].value;
    this.buttons[11] = controller.buttons[11].value;
    this.buttons[12] = controller.buttons[12].value;
    this.buttons[13] = controller.buttons[13].value;
    this.buttons[14] = controller.buttons[14].value;
    this.buttons[15] = controller.buttons[15].value;
    this.buttons[16] = controller.buttons[16].value;

    this.axes[0] = controller.axes[0].valueOf();
    this.axes[1] = controller.axes[1].valueOf();
    this.axes[2] = controller.axes[2].valueOf();
    this.axes[3] = controller.axes[3].valueOf();
  }
}
