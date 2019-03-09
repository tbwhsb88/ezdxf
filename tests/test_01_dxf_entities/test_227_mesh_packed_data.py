# Copyright (c) 2018 Manfred Moitzi
# License: MIT License
import pytest
from ezdxf.lldxf.extendedtags import ExtendedTags
from ezdxf.lldxf.tagwriter import TagCollector
from ezdxf.entities.mesh import Mesh
from ezdxf.entities.mesh import create_vertex_array, create_face_list, create_edge_array, create_crease_array
from ezdxf.entities.mesh import face_to_array


@pytest.fixture
def mesh():
    return Mesh.from_text(MESH)


@pytest.fixture
def mesh_tags():
    return ExtendedTags.from_text(MESH).subclasses[2]


def test_mesh_geometric_data(mesh):
    with mesh.edit_data() as mesh_data:
        assert 56 == len(mesh_data.vertices)
        assert 54 == len(mesh_data.faces)
        assert 108 == len(mesh_data.edges)
        assert 108 == len(mesh_data.edge_crease_values)


def test_create_vertex_array(mesh_tags):
    start_index = mesh_tags.tag_index(92) + 1
    vertices = create_vertex_array(mesh_tags, start_index)
    assert len(vertices) == 56

    tags = TagCollector.dxftags(vertices)
    assert len(tags) == 3 * len(vertices)


def test_create_face_list(mesh_tags):
    start_index = mesh_tags.tag_index(93) + 1
    faces = create_face_list(mesh_tags, start_index)
    assert len(faces) == 54

    tags = TagCollector.dxftags(faces)
    assert tags[0].code == 93
    assert tags[0].value == 270
    assert faces.tag_count() == 270
    # tag count + counter
    assert len(tags) == 271


def test_create_edge_array(mesh_tags):
    start_index = mesh_tags.tag_index(94) + 1
    edges = create_edge_array(mesh_tags, start_index)
    assert len(edges) == 108

    tags = TagCollector.dxftags(edges)
    assert tags[0].code == 94
    assert tags[0].value == 108
    # always two tags per edge + counter
    assert len(tags) == 217


def test_create_crease_array(mesh_tags):
    start_index = mesh_tags.tag_index(95) + 1
    creases = create_crease_array(mesh_tags, start_index)
    assert len(creases) == 108


def test_face_indices_as_array():
    a = face_to_array([0, 1, 2, 3])
    assert a.typecode == 'B'

    a = face_to_array([0, 1, 2, 512])
    assert a.typecode == 'I'

    a = face_to_array([0, 1, 2, 100000])
    assert a.typecode == 'L'


MESH = """  0
MESH
5
2E2
330
1F
100
AcDbEntity
8
0
100
AcDbSubDMesh
71
2
72
0
91
3
92
56
10
284.7875769672455
20
754.2780370501814
30
64.23540699023241
10
284.7875769672455
20
754.2780370501814
30
0.0
10
284.7875769672455
20
616.8856749189314
30
64.23540699023241
10
284.7875769672455
20
616.8856749189314
30
0.0
10
284.7875769672455
20
360.4098446797661
30
193.4439639884759
10
284.7875769672455
20
479.4933127876815
30
0.0
10
284.7875769672455
20
463.228394722746
30
102.3121531918951
10
284.7875769672455
20
342.1009506564315
30
0.0
10
427.8287432817834
20
754.2780370501814
30
64.23540699023241
10
427.8287432817834
20
754.2780370501814
30
0.0
10
427.8287432817834
20
616.8856749189314
30
64.23540699023241
10
427.8287432817834
20
616.8856749189314
30
0.0
10
427.8287432817834
20
360.4098446797661
30
193.4439639884759
10
427.8287432817834
20
479.4933127876815
30
0.0
10
427.8287432817834
20
463.228394722746
30
102.3121531918951
10
427.8287432817834
20
342.1009506564315
30
0.0
10
570.8699095963213
20
754.2780370501814
30
64.23540699023241
10
570.8699095963213
20
754.2780370501814
30
0.0
10
570.8699095963213
20
616.8856749189314
30
64.23540699023241
10
570.8699095963213
20
616.8856749189314
30
0.0
10
570.8699095963213
20
360.4098446797661
30
193.4439639884759
10
570.8699095963213
20
479.4933127876815
30
0.0
10
570.8699095963213
20
463.228394722746
30
102.3121531918951
10
570.8699095963213
20
342.1009506564315
30
0.0
10
713.9110759108594
20
754.2780370501814
30
64.23540699023241
10
713.9110759108594
20
754.2780370501814
30
0.0
10
713.9110759108594
20
616.8856749189314
30
64.23540699023241
10
713.9110759108594
20
616.8856749189314
30
0.0
10
713.9110759108594
20
360.4098446797661
30
193.4439639884759
10
713.9110759108594
20
479.4933127876815
30
0.0
10
713.9110759108594
20
463.228394722746
30
102.3121531918951
10
713.9110759108594
20
342.1009506564315
30
0.0
10
427.8287432817834
20
342.1009506564315
30
21.41180233007747
10
427.8287432817834
20
754.2780370501814
30
21.41180233007747
10
427.8287432817834
20
342.1009506564315
30
42.82360466015493
10
427.8287432817834
20
754.2780370501814
30
42.82360466015493
10
570.8699095963213
20
342.1009506564315
30
21.41180233007747
10
570.8699095963213
20
754.2780370501814
30
21.41180233007747
10
570.8699095963213
20
342.1009506564315
30
42.82360466015493
10
570.8699095963213
20
754.2780370501814
30
42.82360466015493
10
713.9110759108594
20
616.8856749189314
30
21.41180233007747
10
284.7875769672455
20
616.8856749189314
30
21.41180233007747
10
713.9110759108594
20
616.8856749189314
30
42.82360466015493
10
284.7875769672455
20
616.8856749189314
30
42.82360466015493
10
713.9110759108594
20
479.4933127876815
30
21.41180233007747
10
284.7875769672455
20
479.4933127876815
30
21.41180233007747
10
713.9110759108594
20
479.4933127876815
30
42.82360466015493
10
284.7875769672455
20
479.4933127876815
30
42.82360466015493
10
284.7875769672455
20
754.2780370501814
30
21.41180233007747
10
284.7875769672455
20
342.1009506564315
30
21.41180233007747
10
713.9110759108594
20
754.2780370501814
30
21.41180233007747
10
713.9110759108594
20
342.1009506564315
30
21.41180233007747
10
284.7875769672455
20
754.2780370501814
30
42.82360466015493
10
284.7875769672455
20
342.1009506564315
30
42.82360466015493
10
713.9110759108594
20
754.2780370501814
30
42.82360466015493
10
713.9110759108594
20
342.1009506564315
30
42.82360466015493
93
270
90
4
90
2
90
10
90
8
90
0
90
4
90
4
90
12
90
10
90
2
90
4
90
6
90
14
90
12
90
4
90
4
90
10
90
18
90
16
90
8
90
4
90
12
90
20
90
18
90
10
90
4
90
14
90
22
90
20
90
12
90
4
90
18
90
26
90
24
90
16
90
4
90
20
90
28
90
26
90
18
90
4
90
22
90
30
90
28
90
20
90
4
90
1
90
9
90
11
90
3
90
4
90
3
90
11
90
13
90
5
90
4
90
5
90
13
90
15
90
7
90
4
90
9
90
17
90
19
90
11
90
4
90
11
90
19
90
21
90
13
90
4
90
13
90
21
90
23
90
15
90
4
90
17
90
25
90
27
90
19
90
4
90
19
90
27
90
29
90
21
90
4
90
21
90
29
90
31
90
23
90
4
90
15
90
32
90
49
90
7
90
4
90
32
90
34
90
53
90
49
90
4
90
34
90
14
90
6
90
53
90
4
90
23
90
36
90
32
90
15
90
4
90
36
90
38
90
34
90
32
90
4
90
38
90
22
90
14
90
34
90
4
90
31
90
51
90
36
90
23
90
4
90
51
90
55
90
38
90
36
90
4
90
55
90
30
90
22
90
38
90
4
90
48
90
33
90
9
90
1
90
4
90
52
90
35
90
33
90
48
90
4
90
0
90
8
90
35
90
52
90
4
90
33
90
37
90
17
90
9
90
4
90
35
90
39
90
37
90
33
90
4
90
8
90
16
90
39
90
35
90
4
90
37
90
50
90
25
90
17
90
4
90
39
90
54
90
50
90
37
90
4
90
16
90
24
90
54
90
39
90
4
90
50
90
40
90
27
90
25
90
4
90
54
90
42
90
40
90
50
90
4
90
24
90
26
90
42
90
54
90
4
90
40
90
44
90
29
90
27
90
4
90
42
90
46
90
44
90
40
90
4
90
26
90
28
90
46
90
42
90
4
90
44
90
51
90
31
90
29
90
4
90
46
90
55
90
51
90
44
90
4
90
28
90
30
90
55
90
46
90
4
90
1
90
3
90
41
90
48
90
4
90
48
90
41
90
43
90
52
90
4
90
52
90
43
90
2
90
0
90
4
90
3
90
5
90
45
90
41
90
4
90
41
90
45
90
47
90
43
90
4
90
43
90
47
90
4
90
2
90
4
90
5
90
7
90
49
90
45
90
4
90
45
90
49
90
53
90
47
90
4
90
47
90
53
90
6
90
4
94
108
90
2
90
10
90
8
90
10
90
0
90
8
90
0
90
2
90
4
90
12
90
10
90
12
90
2
90
4
90
6
90
14
90
12
90
14
90
4
90
6
90
10
90
18
90
16
90
18
90
8
90
16
90
12
90
20
90
18
90
20
90
14
90
22
90
20
90
22
90
18
90
26
90
24
90
26
90
16
90
24
90
20
90
28
90
26
90
28
90
22
90
30
90
28
90
30
90
1
90
9
90
9
90
11
90
3
90
11
90
1
90
3
90
11
90
13
90
5
90
13
90
3
90
5
90
13
90
15
90
7
90
15
90
5
90
7
90
9
90
17
90
17
90
19
90
11
90
19
90
19
90
21
90
13
90
21
90
21
90
23
90
15
90
23
90
17
90
25
90
25
90
27
90
19
90
27
90
27
90
29
90
21
90
29
90
29
90
31
90
23
90
31
90
15
90
32
90
32
90
49
90
7
90
49
90
32
90
34
90
34
90
53
90
49
90
53
90
14
90
34
90
6
90
53
90
23
90
36
90
32
90
36
90
36
90
38
90
34
90
38
90
22
90
38
90
31
90
51
90
36
90
51
90
51
90
55
90
38
90
55
90
30
90
55
90
33
90
48
90
9
90
33
90
1
90
48
90
35
90
52
90
33
90
35
90
48
90
52
90
8
90
35
90
0
90
52
90
33
90
37
90
17
90
37
90
35
90
39
90
37
90
39
90
16
90
39
90
37
90
50
90
25
90
50
90
39
90
54
90
50
90
54
90
24
90
54
90
40
90
50
90
27
90
40
90
42
90
54
90
40
90
42
90
26
90
42
90
40
90
44
90
29
90
44
90
42
90
46
90
44
90
46
90
28
90
46
90
44
90
51
90
46
90
55
90
3
90
41
90
41
90
48
90
41
90
43
90
43
90
52
90
2
90
43
90
5
90
45
90
41
90
45
90
45
90
47
90
43
90
47
90
4
90
47
90
45
90
49
90
47
90
53
95
108
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
140
0.0
90
0
"""
