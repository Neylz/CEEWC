#version 150

#moj_import <fog.glsl>

uniform sampler2D Sampler0;

uniform vec4 ColorModulator;
uniform float FogStart;
uniform float FogEnd;
uniform vec4 FogColor;

in float vertexDistance;
in vec4 vertexColor;
in vec2 texCoord0;
in vec2 texCoord1;

out vec4 fragColor;

void main() {
    vec4 color;
    if (ivec3(texelFetch(Sampler0, ivec2(63,0), 0).xyz*255) != ivec3(255, 254, 253)) {
        ivec2 texel = ivec2(texCoord0 * textureSize(Sampler0, 0));
        texel -= ivec2(21, 0);
        #moj_import <nlz/elytratex.glsl>
        color = elytra[texel.x + texel.y * 24] * vertexColor * ColorModulator;
    } else color = texture(Sampler0, texCoord0) * vertexColor * ColorModulator;

    if (color.a < 0.1) {
        discard;
    }
    fragColor = linear_fog(color, vertexDistance, FogStart, FogEnd, FogColor);
}